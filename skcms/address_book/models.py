from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number_house = models.IntegerField(verbose_name='Number')
    number_flat = models.IntegerField(null=True, verbose_name='Flat')

    class Meta:
        default_permissions = ()
        select_on_save = True



    def get_absolute_url(self):
        return '/address_book/person/%d' % self.pk

    def __str__(self):
        return self.city + ', ' + self.street + ' ' + str(self.number_house) + '/' + str(self.number_flat)


class Phone(models.Model):
    TYPE_PHONE = (
        (1, "business"),
        (2, "home")
    )
    number_phone = models.CharField(max_length=30)
    type = models.IntegerField(choices=TYPE_PHONE)
    person = models.ForeignKey(to='Person', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return '/address_book/person/%d' % self.pk

    def __str__(self):
        return self.number_phone


class Email(models.Model):
    TYPE_EMAIL = (
        (1, "home"),
        (2, "business"),
    )
    email = models.CharField(max_length=30, default="")
    type = models.IntegerField(choices=TYPE_EMAIL, default=1)
    person = models.ForeignKey(to='Person', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return '/address_book/person/%d' % self.pk

    def __str__(self):
        return self.email


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, null=True)

    class Meta:
        ordering = ['surname', '-name']
        permissions = (
            ("view_person", "Can view person"),
        )

    def get_absolute_url(self):
        return '/address_book/person/%d' % self.pk

    def __str__(self):
        return self.surname + ' ' + self.name



#
#     # this is just required for easy explanation
#     class Meta:
#         app_label = 'permission'
#
# # can add permission logic in this place or perms.py in app
#
# # apply AddressBookPermissionLogic to Person
# from permission import add_permission_logic
# from permission.logics import AuthorPermissionLogic, StaffPermissionLogic
#
# add_permission_logic(Person, AuthorPermissionLogic())
# # add_permission_logic(Person, AuthorPermissionLogic(
# #     field_name='user',
# # ))
