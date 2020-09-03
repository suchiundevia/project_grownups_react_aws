# Import django signals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Receiver that gets the signal and performs an action
from django.dispatch import receiver
from .models import UserProfile


# Decorator
# When a user is saved, a post_save signal is triggered
# The signal is then received by the receiver which is the function below
# The function takes all the information the receiver got as parameters
# Kwargs accepts any additional keywords onto the end of the function

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    # If the user was created then create a UserProfile object with the instance of user that was created
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **kwargs):
    # Save the profile when a user is created
    instance.userprofile.save()
