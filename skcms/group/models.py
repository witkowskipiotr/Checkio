from django.db import models

from address_book.models import Person


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(to=Person, through='GroupPerson')

    def __str__(self):
        return self.name


class GroupPerson(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE, primary_key=True)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.person.name