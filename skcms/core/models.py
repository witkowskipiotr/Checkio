from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return '/address_book/person/%d' % self.pk

    def __repr__(self):
        return 'test'

    __str__ = __repr__


def get_custom_anon_user(User):
    return User(
        username='AnonymousUser',
        birth_date=datetime.date(1410, 7, 15),
    )
