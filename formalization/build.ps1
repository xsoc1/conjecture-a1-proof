# Cached offline Lake build, standard Lake build, or one-file check.
# See PROGRESS.md for the exact command used in this workspace.
param(
  [string]$File = 'ConjectureA1.lean',
  [string]$LeanBin = '',
  [switch]$Mathlib,
  [string]$MathlibCache = ''
)
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $LeanBin) {
  $d = Get-ChildItem (Join-Path $here '.lean') -Directory -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -like 'lean-*windows*' } | Select-Object -First 1
  if ($d) { $LeanBin = Join-Path $d.FullName 'bin' }
}
if (-not $LeanBin -or -not (Test-Path (Join-Path $LeanBin 'lean.exe'))) {
  throw 'Pass -LeanBin <existing toolchain bin directory> or run setup.ps1 locally.'
}
$env:PATH = "$LeanBin;$env:PATH"
Write-Host "lean: $(& (Join-Path $LeanBin 'lean.exe') --version)"
if ($MathlibCache) {
  $cache = (Resolve-Path -LiteralPath $MathlibCache).Path
  $manifest = Get-Content -LiteralPath (Join-Path $here 'lake-manifest.json') -Raw | ConvertFrom-Json
  $pin = ($manifest.packages | Where-Object name -eq 'mathlib').rev
  $head = & git -C $cache rev-parse HEAD
  if ($LASTEXITCODE -ne 0 -or $head -ne $pin) { throw "Cached Mathlib HEAD does not match $pin" }
  if ((& (Join-Path $LeanBin 'lean.exe') --version) -notmatch 'version 4\.31\.0,') {
    throw 'This project requires Lean 4.31.0'
  }
  $paths = @((Join-Path $cache '.lake\build\lib\lean'))
  foreach ($root in @((Split-Path -Parent $cache), (Join-Path $cache '.lake\packages'))) {
    if (Test-Path -LiteralPath $root) {
      Get-ChildItem -LiteralPath $root -Directory | ForEach-Object {
        $p = Join-Path $_.FullName '.lake\build\lib\lean'
        if (Test-Path -LiteralPath $p) { $paths += $p }
      }
    }
  }
  $env:LEAN_PATH = ($paths | Select-Object -Unique) -join ';'
  $env:A1_LEAN = Join-Path $LeanBin 'lean.exe'
  $evidence = Join-Path $here 'evidence'
  New-Item -ItemType Directory -Force -Path $evidence | Out-Null
  @("Lean=$env:A1_LEAN", "Mathlib=$cache", "HEAD=$head", "LEAN_PATH=$env:LEAN_PATH",
    'COMMAND=lake.exe -f lakefile.offline.lean build',
    'External cache paths are read-only imports; generated artifacts stay in this package.') |
    Set-Content -LiteralPath (Join-Path $evidence 'build-context.log')
  Push-Location $here
  try {
    & (Join-Path $LeanBin 'lake.exe') -f lakefile.offline.lean build 2>&1 |
      Tee-Object -FilePath (Join-Path $evidence 'lake-build.log')
    $code = $LASTEXITCODE
    "EXIT=$code" | Tee-Object -FilePath (Join-Path $evidence 'lake-build.log') -Append
    if ($code -ne 0) { throw "Offline Lake proof target failed: $code" }
  } finally { Pop-Location }
} elseif ($Mathlib) {
  Push-Location $here
  try {
    & (Join-Path $LeanBin 'lake.exe') build
    if ($LASTEXITCODE -ne 0) { throw "lake build failed: $LASTEXITCODE" }
  } finally { Pop-Location }
} else {
  & (Join-Path $LeanBin 'lean.exe') (Join-Path $here $File)
  if ($LASTEXITCODE -ne 0) { throw "Lean check failed: $LASTEXITCODE" }
}
