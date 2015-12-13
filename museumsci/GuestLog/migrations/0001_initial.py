# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_of_walkin', models.CharField(default='Adult', max_length=6, choices=[('Senior', 'Senior'), ('Adult', 'Adult'), ('Teenager', 'Teenager'), ('Child', 'Child')])),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ethno_of_walkin', models.CharField(max_length=2, choices=[('AF', 'African-American'), ('W', 'Caucasian'), ('L', 'Mexican-American'), ('I', 'Indian'), ('A', 'Asian'), ('O', 'Other')])),
            ],
        ),
    ]
