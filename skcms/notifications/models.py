# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth import get_user_model
User = get_user_model()


class Notifications(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    viewed = models.BooleanField(default=False, verbose_name="Opened")
    user = models.ForeignKey(to=User)

    def __str__(self):
        return self.title

@receiver(post_save, sender=User)
def send_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notifications.objects.create(user=kwargs.get('instance'),
                                     title="Welcome",
                                     content="This is new notifications")
