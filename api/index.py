import os, sys

# Vercel clones repo to /vercel/path0/
# Our Django app is at /vercel/path0/msresort/
# The msresort package is at /vercel/path0/msresort/msresort/
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
django_root = os.path.join(repo_root, 'msresort')
sys.path.insert(0, django_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msresort.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
