$ErrorActionPreference = 'Stop'

function Normalize-Name([string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) { return '' }
    $d = $Value.Normalize([Text.NormalizationForm]::FormD)
    return (($d -replace '\p{Mn}', '') -replace '[^A-Za-z0-9]', '').ToLowerInvariant()
}

$workspace = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
$naming = Join-Path $workspace 'brand/naming'
$corpus = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)

function Add-CorpusValue([string]$Value) {
    $value = $Value -replace '\*', '' -replace '^⭐\s*', ''
    $n = Normalize-Name $value
    if ($n) { [void]$corpus.Add($n) }
}

# Retained Markdown candidate formats: numbered tables, candidate-first tables, and
# bold candidate bullets. Workbench files are excluded to avoid self-matches.
Get-ChildItem $naming -Recurse -File -Filter '*.md' |
    Where-Object { $_.FullName -notlike '*\workbench-wave34\*' } |
    ForEach-Object {
        foreach ($line in Get-Content $_.FullName -Encoding UTF8) {
            if ($line -match '^\|\s*\d+\s*\|\s*([^|]+)\|') {
                Add-CorpusValue $Matches[1]
            }
            elseif ($line -match '^\|\s*\*\*(?:⭐\s*)?([^*|]+)\*\*\s*\|') {
                Add-CorpusValue $Matches[1]
            }
            if ($line -match '^\s*-\s+\*\*(?:⭐\s*)?([^*]+)\*\*') {
                Add-CorpusValue $Matches[1]
            }
        }
    }

# The calibrated Top-500 workbook is part of the retained historical corpus.
Add-Type -AssemblyName System.IO.Compression.FileSystem
$xlsx = Join-Path $naming 'Top-500-Brand-Names.xlsx'
$zip = [IO.Compression.ZipFile]::OpenRead($xlsx)
try {
    foreach ($entry in $zip.Entries | Where-Object { $_.FullName -like 'xl/worksheets/sheet*.xml' }) {
        $reader = [IO.StreamReader]::new($entry.Open())
        try { [xml]$sheet = $reader.ReadToEnd() } finally { $reader.Dispose() }
        $ns = [Xml.XmlNamespaceManager]::new($sheet.NameTable)
        $ns.AddNamespace('x', 'http://schemas.openxmlformats.org/spreadsheetml/2006/main')
        foreach ($cell in $sheet.SelectNodes('//x:c[@t="inlineStr"]', $ns)) {
            $value = ($cell.SelectNodes('.//x:t', $ns) | ForEach-Object { $_.InnerText }) -join ''
            if ($value.Length -le 80) { Add-CorpusValue $value }
        }
    }
}
finally { $zip.Dispose() }

$raw = Get-Content (Join-Path $PSScriptRoot 'wave3-raw.txt') -Encoding UTF8 |
    Where-Object { $_ -match '^[a-z-]+ \| ' } |
    ForEach-Object {
        $parts = $_ -split ' \| ', 2
        [pscustomobject]@{ Territory = $parts[0]; Name = $parts[1]; Normalized = Normalize-Name $parts[1] }
    }

$rawUnique = $raw | Group-Object Normalized | ForEach-Object { $_.Group[0] }
$rawClean = $rawUnique | Where-Object { -not $corpus.Contains($_.Normalized) }

$result = [ordered]@{
    CorpusNormalized = $corpus.Count
    RawRows = $raw.Count
    RawUniqueNormalized = $rawUnique.Count
    RawExactCorpusCollisions = $rawUnique.Count - $rawClean.Count
    RawCleanSurvivors = $rawClean.Count
}

$selectionPath = Join-Path $PSScriptRoot 'wave3-selection.txt'
if (Test-Path $selectionPath) {
    $selection = Get-Content $selectionPath -Encoding UTF8 |
        Where-Object { $_ -match '^[^#|]+\s\|\s[a-z-]+$' } |
        ForEach-Object {
            $parts = $_ -split '\s\|\s', 2
            [pscustomobject]@{ Name = $parts[0].Trim(); Territory = $parts[1].Trim() }
        }
    $selectionClean = $selection | Where-Object { -not $corpus.Contains((Normalize-Name $_.Name)) }
    $result.SelectionRows = $selection.Count
    $result.SelectionClean = $selectionClean.Count
    $result.SelectionCorpusCollisions = $selection.Count - $selectionClean.Count
}

$poolPath = Join-Path $PSScriptRoot 'wave3-pool.csv'
if (Test-Path $poolPath) {
    $pool = Import-Csv $poolPath
    $poolNorm = $pool | ForEach-Object { Normalize-Name $_.Name }
    $result.PoolRows = $pool.Count
    $result.PoolUniqueNormalized = ($poolNorm | Sort-Object -Unique).Count
    $result.PoolCorpusCollisions = @($pool | Where-Object { $corpus.Contains((Normalize-Name $_.Name)) }).Count
    $result.PoolMinimumScore = ($pool | Measure-Object Score -Minimum).Minimum
    $result.PoolMaximumScore = ($pool | Measure-Object Score -Maximum).Maximum
    $result.PoolTopFlags = @($pool | Where-Object { $_.Top20 -eq 'yes' }).Count
}


if (Test-Path $selectionPath) {
    $selectionCollisions = $selection | Where-Object { $corpus.Contains((Normalize-Name $_.Name)) }
    if ($selectionCollisions) {
        'SELECTION COLLISIONS:'
        $selectionCollisions | Select-Object Name, Territory
    }
}

[pscustomobject]$result | Format-List

if (Test-Path $poolPath) {
    $collisions = $pool | Where-Object { $corpus.Contains((Normalize-Name $_.Name)) }
    if ($collisions) {
        'POOL COLLISIONS:'
        $collisions | Select-Object Rank, Name
    }
}
