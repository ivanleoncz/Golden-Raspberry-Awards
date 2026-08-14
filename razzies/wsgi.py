"""
WSGI config for razzies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from app.utils import database_setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'razzies.settings')

database_setup()

application = get_wsgi_application()
