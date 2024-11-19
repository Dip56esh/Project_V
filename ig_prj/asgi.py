"""
ASGI config for ig_prj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from directs.urls import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ig_prj.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django views
    "websocket": AuthMiddlewareStack(  # WebSocket connections with authentication
        URLRouter(
            websocket_urlpatterns
        )
    ),
})