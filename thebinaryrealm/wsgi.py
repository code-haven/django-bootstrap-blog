"""
WSGI config for thebinaryrealm project.

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thebinaryrealm.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())