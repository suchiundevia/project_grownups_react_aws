from django.contrib import admin
from .models import Activity, News, Interest, VisitorNotification

admin.site.register(Activity)
admin.site.register(News)
admin.site.register(Interest)
admin.site.register(VisitorNotification)