from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number_house = models.IntegerField()
    number_flat = models.IntegerField(null=True)


class Phone(models.Model):
    TYPE_PHONE = (
        (1, "business"),
        (2, "home")
    )
    number_phone = models.CharField(max_length=30)
    type = models.IntegerField(choices=TYPE_PHONE)


class Email(models.Model):
    TYPE_EMAIL = (
        (1, "home"),
        (2, "business"),
    )
    email = models.CharField(max_length=30, default="")
    type = models.IntegerField(choices=TYPE_EMAIL, default=1)


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    address = models.ForeignKey(to=Address, on_delete=None)
    phone = models.ForeignKey(to=Phone, on_delete=None)
    email = models.ForeignKey(to=Email, on_delete=None)


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(to=Person, through='GroupPerson')


class GroupPerson(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
