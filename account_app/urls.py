from django.urls import path
from .views import UserDeleteView
# from . import views

# Direct views used, refer to the global urls.py file
urlpatterns = [
    # Delete account confirmation
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
