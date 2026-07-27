param(
    [Parameter(Mandatory = $true)][string]$InputJson,
    [Parameter(Mandatory = $true)][string]$OutputMarkdown
)

$ErrorActionPreference = 'Stop'

function Escape-MarkdownCell([string]$Value) {
    if ($null -eq $Value) { return '' }
    return $Value.Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
}

function Truncate-Text([string]$Value, [int]$Limit = 180) {
    if ([string]::IsNullOrWhiteSpace($Value) -or $Value.Length -le $Limit) { return $Value }
    return $Value.Substring(0, $Limit - 3) + '...'
}

$rows = @(Get-Content -LiteralPath $InputJson -Raw -Encoding UTF8 | ConvertFrom-Json)
if ($rows.Count -ne 1000) { throw "Expected 1,000 result rows; found $($rows.Count)." }

$groups = $rows | Group-Object decision | Sort-Object Name
$red = @($rows | Where-Object { $_.decision -eq 'RED - OBVIOUS KNOCKOUT' })
$amber = @($rows | Where-Object { $_.decision -eq 'AMBER - REVIEW' })
$yellow = @($rows | Where-Object { $_.decision -eq 'YELLOW - LIVE UNRELATED' })
$pass = @($rows | Where-Object { $_.decision -eq 'PROVISIONAL PASS' })
$queryDate = ($rows.query_date | Sort-Object -Unique) -join ', '

$lines = [Collections.Generic.List[string]]::new()
$lines.Add('# Basic trademark knockout - all 1,000 candidate names')
$lines.Add('')
$lines.Add("> **Query date:** $queryDate")
$lines.Add('>')
$lines.Add('> **Scope:** Official USPTO live full-mark queries for the exact, joined, spaced, and hyphenated forms of every candidate. Results are classified by proximity to cosmetics, skincare, beauty, and coordinated classes. This is a basic knockout only, not clearance, registrability advice, or a legal opinion.')
$lines.Add('')
$lines.Add('## Result summary')
$lines.Add('')
$lines.Add('| Decision | Count | Meaning |')
$lines.Add('|---|---:|---|')
$lines.Add("| RED - obvious knockout | $($red.Count) | Live exact/spacing-normalized mark in IC 003 or clearly related beauty/skincare goods. |")
$lines.Add("| AMBER - review | $($amber.Count) | Live exact/spacing-normalized mark in an adjacent class. |")
$lines.Add("| YELLOW - live unrelated | $($yellow.Count) | Live exact/spacing-normalized federal mark in apparently unrelated goods/services. |")
$lines.Add("| Provisional pass | $($pass.Count) | No live exact/spacing-normalized full-mark hit surfaced. |")
$lines.Add('')
$lines.Add('## Immediate eliminations')
$lines.Add('')
if ($red.Count -eq 0) {
    $lines.Add('No RED exact federal knockouts surfaced in this limited pass.')
    $lines.Add('')
} else {
    $lines.Add('| Set | # | Candidate | Matched mark | Classes | Record |')
    $lines.Add('|---:|---:|---|---|---|---|')
    foreach ($row in $red | Sort-Object set,row) {
        $url = (($row.source_urls -split ' ; ') | Select-Object -First 1)
        $source = if ($url) { "[USPTO record]($url)" } else { '' }
        $lines.Add("| $($row.set) | $($row.row) | $(Escape-MarkdownCell $row.name) | $(Escape-MarkdownCell $row.matched_marks) | $(Escape-MarkdownCell $row.classes) | $source |")
    }
    $lines.Add('')
}

$lines.Add('## Review queue')
$lines.Add('')
$reviewRows = @($amber + $yellow | Sort-Object set,row)
if ($reviewRows.Count -eq 0) {
    $lines.Add('No AMBER or YELLOW exact federal records surfaced.')
    $lines.Add('')
} else {
    $lines.Add('| Set | # | Candidate | Decision | Matched mark | Classes | Record |')
    $lines.Add('|---:|---:|---|---|---|---|---|')
    foreach ($row in $reviewRows) {
        $url = (($row.source_urls -split ' ; ') | Select-Object -First 1)
        $source = if ($url) { "[USPTO record]($url)" } else { '' }
        $lines.Add("| $($row.set) | $($row.row) | $(Escape-MarkdownCell $row.name) | $(Escape-MarkdownCell $row.decision) | $(Escape-MarkdownCell $row.matched_marks) | $(Escape-MarkdownCell $row.classes) | $source |")
    }
    $lines.Add('')
}

$lines.Add('## Complete 1,000-name register')
$lines.Add('')
foreach ($setNumber in 1..4) {
    $setRows = @($rows | Where-Object { $_.set -eq $setNumber } | Sort-Object row)
    $lines.Add("### Set $setNumber")
    $lines.Add('')
    $lines.Add('| # | Name | Score | Federal result | Match / classes | Decision | Source |')
    $lines.Add('|---:|---|---:|---|---|---|---|')
    foreach ($row in $setRows) {
        $match = if ($row.exact_live_hit_count -gt 0) {
            (Escape-MarkdownCell ((Truncate-Text $row.matched_marks 70) + ' / ' + $row.classes))
        } else {
            'None surfaced'
        }
        $url = (($row.source_urls -split ' ; ') | Select-Object -First 1)
        $source = if ($url) { "[USPTO]($url)" } else { '' }
        $lines.Add("| $($row.row) | $(Escape-MarkdownCell $row.name) | $($row.score) | $(Escape-MarkdownCell $row.federal_status) | $match | $(Escape-MarkdownCell $row.decision) | $source |")
    }
    $lines.Add('')
}

$lines.Add('## Limitations and next gate')
$lines.Add('')
$lines.Add('A provisional pass means only that this exact/spacing-normalized live federal query did not surface an obvious record. It does not test every phonetic, visual, semantic, foreign-language, state-register, domain, social, or common-law conflict. It also does not determine whether a name is inherently distinctive or registrable.')
$lines.Add('')
$lines.Add('The strongest survivors still require broader similarity searching, ordinary internet/common-law review, international review where launch is planned, and trademark counsel before filing or material launch spend.')
$lines.Add('')
$lines.Add('- [USPTO: Federal trademark searching](https://www.uspto.gov/trademarks/search/federal-trademark-searching)')
$lines.Add('- [USPTO: Likelihood of confusion](https://www.uspto.gov/trademarks/search/likelihood-confusion)')
$lines.Add('- [USPTO: Comprehensive clearance searches](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks)')

$outputDirectory = Split-Path -Parent $OutputMarkdown
if ($outputDirectory -and -not (Test-Path -LiteralPath $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory | Out-Null
}
$lines | Set-Content -LiteralPath $OutputMarkdown -Encoding UTF8

[pscustomobject]@{
    Output = $OutputMarkdown
    Rows = $rows.Count
    Red = $red.Count
    Amber = $amber.Count
    Yellow = $yellow.Count
    ProvisionalPass = $pass.Count
} | Format-List
