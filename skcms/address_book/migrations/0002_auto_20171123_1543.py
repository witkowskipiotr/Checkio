# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-23 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='person',
        ),
        migrations.RemoveField(
            model_name='groupperson',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupperson',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupPerson',
        ),
    ]