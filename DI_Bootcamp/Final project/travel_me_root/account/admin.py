from django.contrib import admin
from .models import *

admin.site.register(Profile)

admin.site.site_url = '/home'