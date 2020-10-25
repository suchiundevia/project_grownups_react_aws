from django.urls import path
from .views import ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView, \
    UserActivityListView, ManageActivityListView, activity_interest
from . import views

urlpatterns = [
    # List all activities
    path('all/', ActivityListView.as_view(), name='activity-home'),
    # List all activities on map
    path('map/', views.activity_map, name='activity-map'),
    # Activities listed per selected user
    path('user/<str:username>', UserActivityListView.as_view(), name='user-activity'),
    # Detail view of an activity (by primary key or link from the title of list view)
    path('<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    # Manage
    path('<str:username>/manageActivity/', ManageActivityListView.as_view(), name='manage-activity'),
    # Add an activity
    path('new/', ActivityCreateView.as_view(), name='activity-create'),
    # Update an activity
    path('<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    # Delete an activity
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
    # Interest
    path('<int:pk>/interest/', views.activity_interest, name='interest'),
    # People interested
    path('<int:pk>/membersInterested/', views.people_interested, name='people-interested'),
]
