import os, sys

# /vercel/path0/api/index.py  -> go up to /vercel/path0/ then into msresort/
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(root, 'msresort'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'msresort.settings'
os.environ['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'ms-resort-vercel-2026')
os.environ['DEBUG'] = 'False'

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
