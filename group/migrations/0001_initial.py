# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-03 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('set', models.ManyToManyField(blank=True, related_name='set_members', to='set.Set')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
