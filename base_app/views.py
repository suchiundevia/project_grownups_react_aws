from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, '../base_app/templates/base_app/home.html', {'name': 'Test'})


def about(request):
    return render(request, '../base_app/templates/base_app/about.html', {'title': 'About'})
