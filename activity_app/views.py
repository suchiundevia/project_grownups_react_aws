from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Activity, Interest
from account_app.models import Visitor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .utils import Calendar
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
import calendar
from django.utils import timezone


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_app/activity_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


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
              'attendance', 'activity_location', 'activity_suburb', ]

    def form_valid(self, form):
        form.instance.activity_author = self.request.user
        return super().form_valid(form)


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    template_name = 'activity_app/activity_form.html'
    fields = ['activity_title', 'activity_description', 'activity_material', 'activity_start_time', 'activity_end_time',
              'attendance', 'activity_location', 'activity_suburb', ]

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


def activity_interest(request, pk):
    activity = get_object_or_404(Activity, id=pk)
    visitor = get_object_or_404(Visitor, user=request.user)

    if activity.attendance >= Interest.objects.filter(activity_id=activity.id).count():
        interest = Interest(activity=activity, visitor=visitor)
        interest.save()
        return render(request, 'activity_app/activity_interest.html')
    else:
        return render(request, 'activity_app/activity_full.html')


def people_interested(request, pk):
    interests = Interest.objects.filter(activity_id=pk)
    count = interests.count()
    context = {'count': count}
    return render(request, 'activity_app/people_interest.html', context)
