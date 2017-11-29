# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('number_house', models.IntegerField(verbose_name='Number')),
                ('number_flat', models.IntegerField(null=True, verbose_name='Flat')),
            ],
            options={
                'default_permissions': (),
                'select_on_save': True,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=30)),
                ('type', models.IntegerField(choices=[(1, 'home'), (2, 'business')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address_book.Address')),
            ],
            options={
                'ordering': ['surname', '-name'],
                'permissions': (('view_person', 'Can view person'),),
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_phone', models.CharField(max_length=30)),
                ('type', models.IntegerField(choices=[(1, 'business'), (2, 'home')])),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address_book.Person')),
            ],
        ),
    ]
