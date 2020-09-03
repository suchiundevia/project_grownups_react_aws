from django.db import models
from django.contrib.auth.models import User
from PIL import Image


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

    # # The save function runs after the model is saved (inherited to add extra items)
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # Resize large profile pictures uploaded to fit size and reduce storage demand
    #     img = Image.open(self.image.path)
    #     # Max image size wanted is 300px x 300px
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
