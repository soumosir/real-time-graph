from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path
from livedata import consumer

websocker_urlPatterns = [
    path('ws/polData/',consumer.DashConsumer),
]

application = ProtocolTypeRouter({

    'websocket':AuthMiddlewareStack(URLRouter(websocker_urlPatterns))
})