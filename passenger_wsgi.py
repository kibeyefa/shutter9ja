import os
import sys


sys.path.insert(0, "/home/qqjjkxng/test.lumina.com.ng/backend")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shutter9ja.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()