from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('account.urls')),
    path('', include('mainpage.urls')),
    # path('', include('add_flight.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
