# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-28 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('alias', models.CharField(default='', max_length=10)),
                ('secret_key', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_join', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_invites', to='address_book.Person')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address_book.Person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='person',
            field=models.ManyToManyField(through='group.GroupPerson', to='address_book.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='groupperson',
            unique_together=set([('person', 'group')]),
        ),
    ]
