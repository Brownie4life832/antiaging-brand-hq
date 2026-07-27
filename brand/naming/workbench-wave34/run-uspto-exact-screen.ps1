param(
    [string[]]$Reports = @(
        'brand/naming/net-new-250-2026-07-16.md',
        'brand/naming/net-new-250-wave2-2026-07-16.md',
        'brand/naming/net-new-250-wave3-2026-07-16.md',
        'brand/naming/net-new-250-wave4-2026-07-16.md'
    ),

    [Parameter(Mandatory = $true)]
    [string]$OutputJson
)

$ErrorActionPreference = 'Stop'
$Endpoint = 'https://tmsearch.uspto.gov/prod-v1-0-0/tmsearch'
$QueryDate = (Get-Date).ToString('yyyy-MM-dd')

function Get-NormalizedName {
    param([string]$Name)
    $decomposed = $Name.Normalize([Text.NormalizationForm]::FormD)
    return [Text.RegularExpressions.Regex]::Replace($decomposed, '[^A-Za-z0-9]', '').ToLowerInvariant()
}

function Get-ReportRows {
    param([string]$Path, [int]$SetNumber)
    $rows = foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) {
        if ($line -match '^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(\d+\.\d+)\s*\|') {
            $name = $matches[2].Trim()
            [pscustomobject]@{
                set = $SetNumber
                row = [int]$matches[1]
                name = $name
                normalized = Get-NormalizedName $name
                score = [double]$matches[3]
            }
        }
    }
    return @($rows)
}

function ConvertTo-FullMarkClause {
    param([string]$Text)
    $escaped = $Text.Replace('\', '\\').Replace('"', '\"')
    return 'FM:"' + $escaped + '"'
}

function Get-SearchVariants {
    param([string]$Name)
    $variants = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
    [void]$variants.Add($Name)
    if ($Name -match '[\s-]') {
        [void]$variants.Add(($Name -replace '[\s-]+', ''))
        [void]$variants.Add(($Name -replace '[\s-]+', '-'))
        [void]$variants.Add(($Name -replace '[\s-]+', ' '))
    }
    return @($variants)
}

function Invoke-UspToQuery {
    param([string[]]$Names)
    $clauses = foreach ($name in $Names) {
        foreach ($variant in Get-SearchVariants $name) {
            ConvertTo-FullMarkClause $variant
        }
    }
    $queryString = '(' + (($clauses | Sort-Object -Unique) -join ' OR ') + ') AND LD:true'
    $payload = @{
        query = @{
            bool = @{
                must = @(
                    @{
                        query_string = @{
                            query = $queryString
                            default_operator = 'OR'
                        }
                    }
                )
            }
        }
        size = 100
        from = 0
        track_total_hits = $true
        _source = @(
            'id', 'wordmark', 'alive', 'internationalClass',
            'goodsAndServices', 'ownerName', 'registrationId',
            'filedDate', 'registrationDate'
        )
    } | ConvertTo-Json -Depth 12

    for ($attempt = 1; $attempt -le 3; $attempt++) {
        try {
            return Invoke-RestMethod -Uri $Endpoint -Method Post -ContentType 'application/json' -Body $payload
        } catch {
            if ($attempt -eq 3) { throw }
            Start-Sleep -Seconds ([Math]::Pow(2, $attempt - 1))
        }
    }
}

function Invoke-AdaptiveBatch {
    param([object[]]$Rows)
    $response = Invoke-UspToQuery -Names @($Rows.name)
    if ($response.hits.totalValue -ge 100 -and $Rows.Count -gt 1) {
        $mid = [Math]::Floor($Rows.Count / 2)
        $left = @($Rows[0..($mid - 1)])
        $right = @($Rows[$mid..($Rows.Count - 1)])
        return @((Invoke-AdaptiveBatch $left) + (Invoke-AdaptiveBatch $right))
    }
    return @($response.hits.hits)
}

$allRows = @()
for ($i = 0; $i -lt $Reports.Count; $i++) {
    $allRows += Get-ReportRows -Path $Reports[$i] -SetNumber ($i + 1)
}

if ($allRows.Count -ne 1000) {
    throw "Expected 1,000 candidate rows; found $($allRows.Count)."
}
if (($allRows.normalized | Sort-Object -Unique).Count -ne 1000) {
    throw 'Candidate register is not normalized-unique.'
}

$hitsByNormalized = @{}
for ($offset = 0; $offset -lt $allRows.Count; $offset += 20) {
    $last = [Math]::Min($offset + 19, $allRows.Count - 1)
    $batch = @($allRows[$offset..$last])
    Write-Host "USPTO exact/spacing batch $($offset + 1)-$($last + 1) of 1000"
    $hits = Invoke-AdaptiveBatch $batch
    foreach ($hit in $hits) {
        $source = $hit.source
        $normalized = Get-NormalizedName ([string]$source.wordmark)
        if (-not $hitsByNormalized.ContainsKey($normalized)) {
            $hitsByNormalized[$normalized] = [Collections.Generic.List[object]]::new()
        }
        $hitsByNormalized[$normalized].Add($source)
    }
    Start-Sleep -Milliseconds 350
}

$adjacentClasses = @('IC 005', 'IC 010', 'IC 021', 'IC 035', 'IC 042', 'IC 044')
$categoryPattern = '(?i)skin\s*care|skincare|cosmetic|beauty|serum|moisturi[sz]er|facial|dermat|personal care|spa services'

$results = foreach ($row in $allRows) {
    $hitRecords = if ($hitsByNormalized.ContainsKey($row.normalized)) {
        @($hitsByNormalized[$row.normalized])
    } else {
        @()
    }
    $classes = @($hitRecords | ForEach-Object { $_.internationalClass } | Sort-Object -Unique)
    $goods = @($hitRecords | ForEach-Object { $_.goodsAndServices } | Sort-Object -Unique)
    $serials = @($hitRecords | ForEach-Object { $_.id } | Sort-Object -Unique)
    $registrations = @($hitRecords | ForEach-Object { $_.registrationId } | Where-Object { $_ } | Sort-Object -Unique)
    $class3 = $classes -contains 'IC 003'
    $adjacent = @($classes | Where-Object { $_ -in $adjacentClasses }).Count -gt 0
    $categoryGoods = (($goods -join ' ') -match $categoryPattern)

    if ($hitRecords.Count -eq 0) {
        $decision = 'PROVISIONAL PASS'
        $federalStatus = 'No live exact or spacing-normalized full-mark hit'
    } elseif ($class3 -or $categoryGoods) {
        $decision = 'RED - OBVIOUS KNOCKOUT'
        $federalStatus = 'Live exact/spacing-normalized mark in cosmetics, skincare, beauty, or closely described goods'
    } elseif ($adjacent) {
        $decision = 'AMBER - REVIEW'
        $federalStatus = 'Live exact/spacing-normalized mark in an adjacent class'
    } else {
        $decision = 'YELLOW - LIVE UNRELATED'
        $federalStatus = 'Live exact/spacing-normalized federal mark in apparently unrelated goods/services'
    }

    [pscustomobject]@{
        set = $row.set
        row = $row.row
        name = $row.name
        score = $row.score
        query_date = $QueryDate
        federal_status = $federalStatus
        exact_live_hit_count = $hitRecords.Count
        matched_marks = (@($hitRecords | ForEach-Object { $_.wordmark } | Sort-Object -Unique) -join '; ')
        serial_numbers = ($serials -join '; ')
        registration_numbers = ($registrations -join '; ')
        classes = ($classes -join '; ')
        goods_services = (($goods | Select-Object -First 5) -join ' | ')
        source_urls = (@($serials | Select-Object -First 5 | ForEach-Object {
            "https://tsdr.uspto.gov/#caseNumber=$_&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch"
        }) -join ' ; ')
        decision = $decision
        confidence = if ($hitRecords.Count) { 'High for exact/spacing-normalized live federal match' } else { 'High for exact live federal query only' }
        notes = 'Basic knockout only; no availability conclusion; similarity and common-law review remain.'
    }
}

$outputDirectory = Split-Path -Parent $OutputJson
if ($outputDirectory -and -not (Test-Path -LiteralPath $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory | Out-Null
}
$results | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $OutputJson -Encoding UTF8

$summary = $results | Group-Object decision | Sort-Object Name | ForEach-Object {
    [pscustomobject]@{ Decision = $_.Name; Count = $_.Count }
}
$summary | Format-Table -AutoSize
