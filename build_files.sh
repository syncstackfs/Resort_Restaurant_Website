pip install -r requirements.txt
python msresort/manage.py collectstatic --noinput --settings=msresort.settings
python msresort/manage.py migrate --noinput --settings=msresort.settings
