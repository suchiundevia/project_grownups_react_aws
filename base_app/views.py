from django.shortcuts import render
from activity_app.models import Activity
from datetime import datetime, timedelta
from django.utils import timezone


def home(request):
    today = timezone.now()
    activities = Activity.objects.filter(activity_post_date__month=today.month).order_by('-activity_post_date')
    return render(request, 'base_app/home.html', {'activities': activities})

def about(request):
    return render(request, 'base_app/about.html', {'title': 'About'})
