param(
    [Parameter(Mandatory = $true)][string]$PoolCsv,
    [Parameter(Mandatory = $true)][string]$OutputMarkdown,
    [Parameter(Mandatory = $true)][string]$CutsFile,
    [Parameter(Mandatory = $true)][int]$WaveNumber,
    [Parameter(Mandatory = $true)][string]$ScopeText,
    [Parameter(Mandatory = $true)][string]$MethodText
)

$ErrorActionPreference = 'Stop'

function Escape-MarkdownCell([string]$Value) {
    if ($null -eq $Value) { return '' }
    return $Value.Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
}

$pool = @(Import-Csv -LiteralPath $PoolCsv | Sort-Object { [int]$_.Rank })
if ($pool.Count -ne 300) { throw "Expected 300 pool rows; found $($pool.Count)." }
$cuts = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($cut in Get-Content -LiteralPath $CutsFile -Encoding UTF8) {
    if (-not [string]::IsNullOrWhiteSpace($cut)) {
        $cutNormalized = [regex]::Replace($cut.Normalize([Text.NormalizationForm]::FormD), '[^A-Za-z0-9]', '').ToLowerInvariant()
        [void]$cuts.Add($cutNormalized)
    }
}
if ($cuts.Count -ne 50) { throw "Expected 50 unique cuts; found $($cuts.Count)." }

$selected = @($pool | Where-Object {
    $candidateNormalized = [regex]::Replace($_.Name.Normalize([Text.NormalizationForm]::FormD), '[^A-Za-z0-9]', '').ToLowerInvariant()
    -not $cuts.Contains($candidateNormalized)
})
if ($selected.Count -ne 250) { throw "Expected 250 survivors after cuts; found $($selected.Count)." }

$normalized = $selected | ForEach-Object {
    [regex]::Replace($_.Name.Normalize([Text.NormalizationForm]::FormD), '[^A-Za-z0-9]', '').ToLowerInvariant()
}
if (($normalized | Sort-Object -Unique).Count -ne 250) {
    throw 'Selected names are not normalized-unique.'
}
$minimumScore = ($selected.Score | ForEach-Object { [double]$_ } | Measure-Object -Minimum).Minimum
if ($minimumScore -le 8.0) { throw "Minimum score is not strictly above 8.0: $minimumScore" }

$lines = [Collections.Generic.List[string]]::new()
$lines.Add("# 250 additional net-new anti-aging brand names - wave $WaveNumber")
$lines.Add('')
$lines.Add("> **Scope:** $ScopeText")
$lines.Add('>')
$lines.Add("> **Score meaning:** Creative-fit score for this specific brand before trademark, common-law, domain, social, linguistic, or regulatory clearance. Every score is strictly above 8.0/10. A high score is not an availability claim.")
$lines.Add('')
$lines.Add('## Creative winners before the knockout search')
$lines.Add('')
$lines.Add('These are the 12 directions I would react to first as names. The later 1,000-name knockout register - not this creative ranking - controls obvious conflict eliminations.')
$lines.Add('')
for ($i = 0; $i -lt 12; $i++) {
    $lines.Add("$($i + 1). **$($selected[$i].Name)**")
}
$lines.Add('')
$lines.Add('## What changed in this wave')
$lines.Add('')
$lines.Add($MethodText)
$lines.Add('')

for ($start = 0; $start -lt 250; $start += 25) {
    $first = $start + 1
    $last = $start + 25
    $lines.Add("## $first-$last")
    $lines.Add('')
    $lines.Add('| # | Name | Score | Method | Why it earned the score |')
    $lines.Add('|---:|---|---:|---|---|')
    for ($i = $start; $i -lt $last; $i++) {
        $row = $selected[$i]
        $method = if ($row.PSObject.Properties.Name -contains 'Territory') { $row.Territory } else { $row.Method }
        $nameCell = Escape-MarkdownCell $row.Name
        $methodCell = Escape-MarkdownCell $method
        $rationaleCell = Escape-MarkdownCell $row.Rationale
        $lines.Add("| $($i + 1) | $nameCell | $($row.Score) | $methodCell | $rationaleCell |")
    }
    $lines.Add('')
}

$lines.Add('## Screening note')
$lines.Add('')
$lines.Add('All 250 passed normalized retained-corpus exact deduplication, internal deduplication, cross-wave deduplication, and manual brief-fit review. The complete 1,000-name register receives a separate basic federal and live-market knockout. That screen is designed only to remove immediate problems; it is not comprehensive clearance or a legal opinion.')
$lines.Add('')
$lines.Add('USPTO guidance explains that a real clearance search must consider similarity in sound, appearance, meaning, and overall commercial impression for related goods and services, and should extend beyond federal registrations to internet and other common-law sources.')
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
    Rows = $selected.Count
    UniqueNormalized = ($normalized | Sort-Object -Unique).Count
    MinimumScore = $minimumScore
    MaximumScore = ($selected.Score | ForEach-Object { [double]$_ } | Measure-Object -Maximum).Maximum
} | Format-List
