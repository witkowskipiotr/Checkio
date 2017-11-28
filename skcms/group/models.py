import datetime
from django.db import models

from address_book.models import Person


class Group(models.Model):
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=10, default='')
    secret_key = models.CharField(max_length=25, null=True)
    person = models.ManyToManyField(to=Person,
                                     through='GroupPerson',
                                     through_fields=('group', 'person'),
                                     )

    def get_absolute_url(self):
        return '/address_book/group/%d' % self.pk

    def __str__(self):
        return self.name


class GroupPerson(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    inviter = models.ForeignKey(to=Person,
                                on_delete=models.CASCADE,
                                related_name="membership_invites",
                                )
    data_join = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("person", "group"),)

    def save(self, *args, **kwargs):
        related_exists = GroupPerson.objects.filter(group_id=self.group_id,
                                                    person_id=self.person_id)
        if not related_exists:
            super(GroupPerson, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/address_book/person/%d' % self.pk

    def __str__(self):
        return self.person.name
