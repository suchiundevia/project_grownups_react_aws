from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from account_app.models import Visitor


class Activity(models.Model):
    activity_title = models.CharField(max_length=150, null=True, blank=True)
    activity_description = models.TextField(null=True, blank=True)
    activity_material = models.CharField(max_length=250, null=True, blank=True)
    activity_start_time = models.DateTimeField(null=True, blank=True)
    activity_end_time = models.DateTimeField(null=True, blank=True)
    activity_post_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    activity_location = models.CharField(max_length=150, null=True, blank=True)
    activity_suburb = models.CharField(max_length=50, null=True, blank=True)
    activity_author = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.activity_title)

    @property
    def get_html_url(self):
        url = reverse('activity-detail', args=(self.id,))
        return f'<a class="btn btn-danger" href="{url}">{self.activity_title}</a>'

    class Meta:
        verbose_name_plural = 'Activities'


class Interest(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.activity)

    class Meta:
        verbose_name_plural = 'Interest'


class VisitorNotification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(default='Your RSVP is complete')
    notification_date = models.DateTimeField()
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.message)

    class Meta:
        verbose_name_plural = 'InterestNotifications'
