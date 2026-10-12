param(
  [Parameter(Mandatory=$true)][ValidateSet('codex','claude','hermes')][string]$HostName,
  [Parameter(Mandatory=$true)][string]$Destination
)
& python (Join-Path $PSScriptRoot 'scripts/install.py') --host $HostName --destination $Destination
exit $LASTEXITCODE
