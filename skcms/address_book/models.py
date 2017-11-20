from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number_house = models.IntegerField()
    number_flat = models.IntegerField(null=True)

    def __unicode__(self):
        return self.city

class Phone(models.Model):
    TYPE_PHONE = (
        (1, "business"),
        (2, "home")
    )
    number_phone = models.CharField(max_length=30)
    type = models.IntegerField(choices=TYPE_PHONE)

    def __unicode__(self):
        return self.number_phone


class Email(models.Model):
    TYPE_EMAIL = (
        (1, "home"),
        (2, "business"),
    )
    email = models.CharField(max_length=30, default="")
    type = models.IntegerField(choices=TYPE_EMAIL, default=1)

    def __unicode__(self):
        return self.email


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    phone = models.ForeignKey(to=Phone, on_delete=None)
    email = models.ForeignKey(to=Email, on_delete=None)

    def __unicode__(self):
        return self.surname + ' ' + self.name


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(to=Person, through='GroupPerson')

    def __unicode__(self):
        return self.name


class GroupPerson(models.Model):
    id = models.IntegerField(primary_key=True, default=0, editable=False)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
