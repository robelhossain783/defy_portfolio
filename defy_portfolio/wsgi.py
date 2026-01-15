"""
WSGI config for defy_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'defy_portfolio.settings')
#
# application = get_wsgi_application()
#
# # For Vercel
# app = application

import os
import sys

# Project path
path = '/home/robel783/defy_portfolio'
if path not in sys.path:
    sys.path.append(path)

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'defy_portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()