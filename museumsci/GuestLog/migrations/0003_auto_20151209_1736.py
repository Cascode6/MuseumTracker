# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestLog', '0002_auto_20151207_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='Grade',
            field=models.CharField(max_length=2, choices=[('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'fourth'), ('Middle', 'fifth-eigth'), ('High', 'Ninth-Twelfth')]),
        ),
        migrations.AlterField(
            model_name='walk_in',
            name='Age',
            field=models.CharField(max_length=10, choices=[('Senior', 'Senior'), ('Adult', 'Adult'), ('Teen', 'Teen'), ('Child', 'Child')]),
        ),
        migrations.AlterField(
            model_name='walk_in',
            name='Ethnic_background',
            field=models.CharField(max_length=10, choices=[('Indian', 'Indian'), ('Black', 'Black'), ('White', 'White'), ('Latin-American', 'Latin-American'), ('Asian', 'Asian')]),
        ),
    ]
