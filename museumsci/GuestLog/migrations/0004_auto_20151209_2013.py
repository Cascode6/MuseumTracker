# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('GuestLog', '0003_auto_20151209_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='walk_in',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='group',
            name='Grade',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('Middle', 'Middle School'), ('High', 'High School')], max_length=2),
        ),
    ]
