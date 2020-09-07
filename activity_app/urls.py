from django.urls import path
from .views import ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView, \
    UserActivityListView
# from . import views

urlpatterns = [
    # List all activities
    # as_view() required to convert class into a view
    path('all/', ActivityListView.as_view(), name='activity-home'),
    # Activities listed per selected user
    path('user/<str:username>', UserActivityListView.as_view(), name='user-activity'),
    # Detail view of an activity (by primary key or link from the title of list view)
    path('<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    # Add an activity
    path('new/', ActivityCreateView.as_view(), name='activity-create'),
    # Update an activity
    path('<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    # Delete an activity
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
]
