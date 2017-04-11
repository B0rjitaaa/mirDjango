# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ExceptionMessage(models.Model):
	"""docstring for Exception"""

	code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

	date = models.DateTimeField(auto_now=False)

	detail = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

	def __str__(self):
		return str(self.date) + self.detail