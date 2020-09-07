from django.shortcuts import render


# Create your views here.
def view_activity(request):
    return render(request, 'activity_app/activity_home.html')
