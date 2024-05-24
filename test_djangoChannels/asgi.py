"""
ASGI config for test_djangoChannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from app.routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_djangoChannels.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': application,
    "websocket": URLRouter(websocket_urlpatterns)
})
