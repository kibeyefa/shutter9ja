import os
import sys


sys.path.insert(0, "/home/bnamzzfo/backend.shutter9ja.org")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shutter9ja.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()