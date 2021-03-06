# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2022-02-08 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_date', models.DateTimeField(max_length=20, unique=True)),
                ('start_time', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('end_time', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.Theatre'),
        ),
    ]
