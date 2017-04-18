# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170418_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExceptionMessageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('plant_id', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exceptionmessage',
            name='api_name',
        ),
        migrations.RemoveField(
            model_name='exceptionmessage',
            name='date',
        ),
        migrations.AddField(
            model_name='exceptionmessagedetail',
            name='exception_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ExceptionMessage'),
        ),
        migrations.AddField(
            model_name='exceptionmessage',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Source'),
        ),
    ]
