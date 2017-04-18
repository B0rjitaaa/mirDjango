# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Source(models.Model):
    api_name = models.CharField(
            max_length=50,
            blank=True,
            null=True
        )

    def __str__(self):
        return self.api_name


class ExceptionMessage(models.Model):
    source = models.ForeignKey(
            Source,
            on_delete=models.CASCADE,
            blank=True,
            null=True
        )

    code = models.CharField(
            max_length=100,
            blank=True,
            null=True
        )

    detail = models.CharField(
            max_length=200,
            blank=True,
            null=True
        )

    def __str__(self):
        # return self.api_name + '-' + str(self.date) + ' ' + self.code
        return self.code + ' ' + self.detail


class ExceptionMessageDetail(models.Model):
    exception_message = models.ForeignKey(
            ExceptionMessage,
            on_delete=models.CASCADE
        )

    date = models.DateTimeField(auto_now=False)

    plant_id = models.IntegerField(
            blank=True,
            null=True
        )

    region = models.CharField(
            max_length=10,
            null=True,
            blank=True
        )

    def __str__(self):
        return self.plant_id + ' ' + str(self.date)
