"""
WSGI config for razzies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import logging
import os

from django.db import connection
from django.conf import settings
from django.core.wsgi import get_wsgi_application

from app.utils import database_setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'razzies.settings')

log = logging.getLogger()
log.info(f"DEBUG is {settings.DEBUG}")
log.info(f"Database is {settings.DATABASES["default"]["NAME"]}")

# Ensure the DB preparation at runserver startup, specially for "in-memory" DB.
# Persistent DB like "db.sqlite3", already prepared with Django + App migrations,
# will not require further DB setup process.
tables = connection.introspection.table_names()
if not "auth_user" in tables or not tables[0].startswith("app_"):
    database_setup()

application = get_wsgi_application()
