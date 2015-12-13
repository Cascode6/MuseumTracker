# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestLog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('New_Group', models.BooleanField()),
                ('Number_of_Teachers', models.IntegerField()),
                ('Number_of_Chaperones', models.IntegerField()),
                ('Number_of_Students', models.IntegerField()),
                ('School', models.CharField(max_length=10)),
                ('Grade', models.CharField(max_length=1, choices=[('1', 'first'), ('2', 'second'), ('3', 'third')])),
                ('Museum_Program', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Walk_in',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Number_of_guests', models.IntegerField()),
                ('Age', models.CharField(max_length=10)),
                ('Ethnic_background', models.CharField(max_length=10)),
                ('Returning_Guest', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='Ethnicity',
        ),
    ]
