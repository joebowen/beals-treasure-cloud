"""
WSGI config for BealsTreasure project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import sys  # @NoMove

sys.path.insert(1, '..')  # @NoMove

from django.core.wsgi import get_wsgi_application  # @IgnorePep8
import os  # @IgnorePep8


os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "settings")

application = get_wsgi_application()
