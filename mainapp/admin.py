from django.contrib import admin

from .models import Choice, Profile

admin.site.register(Profile)
admin.site.register(Choice)
