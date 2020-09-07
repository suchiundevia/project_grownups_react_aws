from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Activity(models.Model):
    ActivityTitle = models.CharField(max_length=150)
    ActivityDescription = models.TextField()
    ActivityMaterial = models.CharField(max_length=250)
    ActivityStartTime = models.DateTimeField()
    ActivityEndTime = models.DateTimeField()
    ActivityPostDate = models.DateTimeField(default=timezone.now)
    ActivityLocation = models.CharField(max_length=250)
    ActivityAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ActivityTitle

    # Redirect page
    def get_absolute_url(self):
        # Reverse returns the full path as a string
        return reverse('activity-detail', kwargs={'pk': self.pk})
