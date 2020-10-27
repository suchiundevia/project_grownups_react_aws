from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import ActivityListView, NewsListView, UserActivityListView, ActivityDetailView, ActivityCreateView, \
    ActivityUpdateView, ActivityDeleteView, people_interested, activity_interest
from .models import Activity, News


class TestUrls(SimpleTestCase):

    def test_activity_list_view_url(self):
        url = reverse('activity-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ActivityListView)

    def test_news_list_view_url(self):
        url = reverse('news-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NewsListView)

    def test_user_activity_list_view_url(self):
        url = reverse('user-activity', args=['such'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserActivityListView)

    def test_activity_detail_view_url(self):
        url = reverse('activity-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ActivityDetailView)

    def test_activity_create_view_url(self):
        url = reverse('activity-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ActivityCreateView)

    def test_activity_update_view_url(self):
        url = reverse('activity-update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ActivityUpdateView)

    def test_activity_delete_view_url(self):
        url = reverse('activity-delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ActivityDeleteView)

