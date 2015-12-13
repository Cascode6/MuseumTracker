# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestLog', '0004_auto_20151209_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='Grade',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('Middle', 'Middle School'), ('High', 'High School')], max_length=1),
        ),
    ]
