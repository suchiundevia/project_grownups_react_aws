from django.contrib import admin
from .models import UserProfile, Visitor


admin.site.register(UserProfile)
admin.site.register(Visitor)