# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-23 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20171123_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupperson',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='group.Group'),
        ),
    ]