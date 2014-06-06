import os, sys
sys.path.append('/srv/django/main')

os.environ['DJANGO_SETTINGS_MODULE'] = 'siteconfig.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
