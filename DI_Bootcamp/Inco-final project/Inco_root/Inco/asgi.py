import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Inco.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Inco.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Inco.routing.websocket_urlpatterns
        )
    ),