# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = models.CharField(max_length=150, verbose_name="Country")
    age = models.CharField(max_length=3, verbose_name="Age")

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def add_user_profile_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfile.objects.create(user=kwargs.get('instance'))

