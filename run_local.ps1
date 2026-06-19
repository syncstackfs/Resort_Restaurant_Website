# Run the site locally (Windows)
$env:DEBUG = "True"
Set-Location $PSScriptRoot
python msresort/manage.py runserver
