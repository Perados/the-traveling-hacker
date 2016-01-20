# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('handle', models.CharField(default='', blank=True, max_length=100)),
                ('twits', models.CharField(default='', blank=True, max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
