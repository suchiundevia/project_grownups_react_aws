from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_app/activity_home.html'
    context_object_name = 'activities'
    ordering = ['-activity_post_date']
    paginate_by = 2


class UserActivityListView(ListView):
    model = Activity
    template_name = 'activity_app/user_activity.html'
    context_object_name = 'activities'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Activity.objects.filter(activity_author=user).order_by('-activity_post_date')


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_app/activity_detail.html'


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    template_name = 'activity_app/activity_form.html'
    fields = ['activity_title', 'activity_description', 'activity_material', 'activity_start_time', 'activity_end_time',
              'activity_location']

    def form_valid(self, form):
        form.instance.activity_author = self.request.user
        return super().form_valid(form)


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    template_name = 'activity_app/activity_form.html'
    fields = ['activity_title', 'activity_description', 'activity_material', 'activity_start_time', 'activity_end_time',
              'activity_location', 'activity_suburb',]

    def form_valid(self, form):
        form.instance.activity_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.activity_author:
            return True
        else:
            return False


class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    success_url = '/'
    template_name = 'activity_app/activity_delete.html'

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.activity_author:
            return True
        else:
            return False


class ManageActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'activity_app/manage_activity.html'
    context_object_name = 'activities'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Activity.objects.filter(activity_author=user)
