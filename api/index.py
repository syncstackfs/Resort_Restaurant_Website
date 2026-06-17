import os
import sys

# Add the msresort directory to Python path
# From api/index.py, go up one level (..) then into msresort/
msresort_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'msresort')
msresort_dir = os.path.abspath(msresort_dir)

sys.path.insert(0, msresort_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msresort.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
