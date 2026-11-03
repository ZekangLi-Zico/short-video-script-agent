param(
    [ValidateSet('demo', 'test', 'evaluate', 'live', 'api', 'web')]
    [string]$Mode = 'demo',
    [string]$InputFile = 'examples/inputs/normal.json',
    [string]$Output = 'outputs/latest',
    [int]$Port = 8765
)
$ErrorActionPreference = 'Stop'
$taskPythonCandidates = @(
    (Join-Path $PSScriptRoot '.venv\Scripts\python.exe'),
    (Join-Path ([Environment]::GetFolderPath('UserProfile')) '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe')
)
foreach ($taskCommandName in @('python', 'python3')) {
    $taskCommand = Get-Command $taskCommandName -ErrorAction SilentlyContinue
    if ($taskCommand -and $taskCommand.Source -notmatch 'WindowsApps') {
        $taskPythonCandidates += $taskCommand.Source
    }
}
$taskPython = $taskPythonCandidates | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
if (-not $taskPython) { throw 'Python 3.11+ is required. See README.md for setup.' }
$env:PYTHONUTF8 = '1'
Push-Location -LiteralPath $PSScriptRoot
try {
    switch ($Mode) {
        'web' { & $taskPython -m src.web --port $Port --open }
        'test' { & $taskPython -m scripts.run_tests }
        'evaluate' { & $taskPython -m scripts.evaluate --provider mock --output outputs/evaluation-mock }
        'live' { & $taskPython -m src.cli --provider codex --input $InputFile --output $Output }
        'api' { & $taskPython -m src.cli --provider api --input $InputFile --output $Output }
        default { & $taskPython -m src.cli --provider mock --input $InputFile --output $Output }
    }
    $taskExitCode = $LASTEXITCODE
} finally { Pop-Location }
exit $taskExitCode
