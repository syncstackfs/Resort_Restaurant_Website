import os, sys

# Point to the msresort subfolder where manage.py and settings live
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'msresort')
sys.path.insert(0, os.path.abspath(BASE))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msresort.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
