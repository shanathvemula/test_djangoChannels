from django.urls import re_path
from app.consumers import PostConsumer

websocket_urlpatterns = [
    re_path(r"^post$", PostConsumer.as_asgi())
]
