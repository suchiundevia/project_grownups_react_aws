from django.urls import path
from .views import UserDeleteView, UserListView

urlpatterns = [
    # Delete account
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    # View all users
    path('users/', UserListView.as_view(), name='users'),
]
