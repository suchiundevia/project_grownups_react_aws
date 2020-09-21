from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Activity(models.Model):
    activity_title = models.CharField(max_length=150, null=True, blank=True)
    activity_description = models.TextField(null=True, blank=True)
    activity_material = models.CharField(max_length=250, null=True, blank=True)
    activity_date = models.DateTimeField(null=True, blank=True)
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
        url = reverse('activity-update', args=(self.id,))
        return f'<p>{self.activity_title}</p><a href="{url}">edit</a>'

    class Meta:
        verbose_name_plural = 'Activities'
