from django.contrib import admin
from .models import *
from forum.models import *

admin.site.register(Profile)
admin.site.register(Index)
admin.site.register(Comment)