from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# User profile more attributes (one to one relationship)
class UserProfile(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    about = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    feedback = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.about} UserProfile'