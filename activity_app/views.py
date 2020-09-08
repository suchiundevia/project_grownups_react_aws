from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Activity
# LoginRequiredMixin: Prevent a user from adding an activity if they have not yet logged in (rather than decorator)
# UserPassesTestMixin: Ensure no other user can update or change an activity
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
# # FUNCTION BASED VIEWS
# def view_activity(request):
#     context = {
#         'activities': Activity.objects.all()
#     }
#     return render(request, 'activity_app/activity_home.html', context)


# CLASS BASED VIEWS
# More built in functionality (Types: list, create, detail, update or delete)
# List all activities
class ActivityListView(ListView):
    model = Activity
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'activity_app/activity_home.html'
    context_object_name = 'activities'
    # Activities ordered according to post date newest to oldest
    ordering = ['-activity_post_date']
    # Number of activities displayed per page
    paginate_by = 2


# Activity list by user
class UserActivityListView(ListView):
    model = Activity
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'activity_app/user_activity.html'
    context_object_name = 'activities'
    # Number of activities displayed per page
    paginate_by = 2

    # Query set to be filtered
    def get_queryset(self):
        # If the object exists in the database, it will display otherwise show a 404 error
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Activity.objects.filter(ActivityAuthor=user).order_by('-activity_post_date')


# Detail view of a single activity
class ActivityDetailView(DetailView):
    model = Activity
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'activity_app/activity_detail.html'


# Create an activity
class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'activity_app/activity_form.html'
    fields = ['activity_title', 'activity_description', 'activity_material', 'activity_start_time', 'activity_end_time',
              'activity_location']

    # Add the method for adding the author before the form is submitted as it is a not null field (integrity constraint)
    def form_valid(self, form):
        # Take the instance of the form and set its author to the current user and return form
        form.instance.activity_author = self.request.user
        return super().form_valid(form)


# Update an activity
class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'activity_app/activity_form.html'
    fields = ['activity_title', 'activity_description', 'activity_material', 'activity_start_time', 'activity_end_time',
              'activity_location']

    # Add the method for adding the author before the form is submitted as it is a not null field (integrity constraint)
    def form_valid(self, form):
        # Take the instance of the form and set its author to the current user and return form
        form.instance.activity_author = self.request.user
        return super().form_valid(form)

    # Function for the UserPassesTestMixin to run and check if the user passes the condition
    def test_func(self):
        # Get the activity that is being updated (object)
        activity = self.get_object()
        # If the current logged in user matches the activity author than the activity can be updated
        if self.request.user == activity.activity_author:
            return True
        else:
            return False


# Delete an activity
class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    # On deletion - redirect to home page
    success_url = '/'
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'activity_app/activity_delete.html'

    # Function for the UserPassesTestMixin to run and check if the user passes the condition
    def test_func(self):
        # Get the activity that is being deleted (object)
        activity = self.get_object()
        # If the current logged in user matches the activity author than the activity can be updated
        if self.request.user == activity.activity_author:
            return True
        else:
            return False
