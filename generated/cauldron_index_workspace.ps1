$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$root = Join-Path $env:USERPROFILE 'workspace'
$skipDirs = @('.git','.godot','node_modules','.venv','.venv-1','android','.vscode','assets','audio','sprites','artsources','extracted','models','materials','fonts','icons')
$exts = @('.gd','.py','.js','.ts','.vue','.md','.json','.godot')
$keyword = 'event|domain|deck|bpm|threshold|followup|follow_up|payoff|hook|source_packet|corpus|claude|validate|audit|smoke|bootstrap|tts|audio|manifest|speaker|clip|dashboard|console|command|parser|choice|button|room|swipe|lane|attack|dash|block|parry|hitbox|combo|stomp|ai|conductor|enemy|flee|chase|raider|zombie|spawn|vehicle|road|mph|rpm|tire|slip|skid|fuel|import|glb|blend|asset|attribution|license|pose|rig|bone|skeleton|keyframe|ik|onion|mine|shop|upgrade|crystal|resource|harvest|offer|render|localstorage|save|load|server|draft|report|drift|repetition|chunk|critique|original'
$records = New-Object System.Collections.Generic.List[object]
$files = Get-ChildItem -Path $root -Recurse -File -ErrorAction SilentlyContinue | Where-Object {
  $path = $_.FullName
  $parts = $path.Substring($root.Length).Split([IO.Path]::DirectorySeparatorChar, [StringSplitOptions]::RemoveEmptyEntries)
  -not ($parts | Where-Object { $skipDirs -contains $_ }) -and $exts -contains $_.Extension.ToLowerInvariant() -and $_.Length -lt 650000
} | Select-Object -First 1500
foreach ($file in $files) {
  $rel = $file.FullName.Substring($root.Length).TrimStart('\')
  $project = ($rel -split '\\')[0]
  try { $lines = Get-Content -LiteralPath $file.FullName -ErrorAction Stop } catch { continue }
  for ($i = 0; $i -lt $lines.Count; $i++) {
    $trim = ([string]$lines[$i]).Trim()
    if ([string]::IsNullOrWhiteSpace($trim)) { continue }
    $symbol = ''
    if ($trim -match '^(func|def|function)\s+([A-Za-z_][A-Za-z0-9_]*)') { $symbol = $matches[2] }
    elseif ($file.Extension -eq '.md' -and $trim.StartsWith('#')) { $symbol = $trim.TrimStart('#').Trim() }
    elseif ($file.Extension -eq '.json' -and $trim -match '^"([^"]+)"\s*:') { $symbol = $matches[1] }
    elseif ($file.Name -eq 'project.godot' -and ($trim -like 'config/name=*' -or $trim -like 'run/main_scene=*')) { $symbol = $trim.Split('=')[0].Trim() }
    $hit = $false
    if ($symbol -ne '') { $hit = $true }
    elseif ($trim -match $keyword -and $trim.Length -le 240) { $hit = $true }
    if ($hit -and (($rel + ' ' + $symbol + ' ' + $trim) -match $keyword)) {
      if ($trim.Length -gt 180) { $evidence = $trim.Substring(0,177) + '...' } else { $evidence = $trim }
      $records.Add([pscustomobject]@{
        origin = 'cauldron'
        project = $project
        repo = ''
        path = $rel.Replace('\\','/')
        line = $i + 1
        symbol = $symbol
        evidence = $evidence
        source_url = 'ssh://dclar@192.168.40.213/C:/Users/dclar/workspace/' + $rel.Replace('\\','/') + '#L' + ($i + 1)
      }) | Out-Null
    }
  }
}
$records | ConvertTo-Json -Compress -Depth 5
