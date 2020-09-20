from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, Organiser, Visitor


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


@receiver(post_save, sender=UserProfile)
def create_organiser(sender, instance, created, **kwargs):
    if created:
        Organiser.objects.create(user_profile=instance)


@receiver(post_save, sender=UserProfile)
def save_organiser(sender, instance, **kwargs):
    instance.organiser.save()


@receiver(post_save, sender=UserProfile)
def create_visitor(sender, instance, created, **kwargs):
    if created:
        Visitor.objects.create(user_profile=instance)


@receiver(post_save, sender=UserProfile)
def save_visitor(sender, instance, **kwargs):
    instance.visitor.save()
