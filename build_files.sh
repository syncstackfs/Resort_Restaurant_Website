#!/bin/bash
set -e
pip install -r requirements.txt
python scripts/optimize_assets.py
python msresort/manage.py collectstatic --noinput --clear
python msresort/manage.py migrate --noinput
