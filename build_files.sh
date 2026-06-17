pip install -r requirements.txt
python msresort/manage.py collectstatic --noinput
python msresort/manage.py migrate --noinput
