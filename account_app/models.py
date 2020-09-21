from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    about = models.TextField(null=True, blank=True)
    phone_number = models.CharField(default='6894736528', max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.about} UserProfile'

    class Meta:
        verbose_name_plural = 'User Profile'


class Organiser(models.Model):
    user_profile = models.OneToOneField(UserProfile, default="", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Organiser'


class Visitor(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Visitor'
