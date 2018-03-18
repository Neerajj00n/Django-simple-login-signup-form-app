from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
	firstname = models.CharField(max_length=255, null=True, blank=True)
	lastname = models.CharField(max_length=255, null=True, blank=True)
	email = models.CharField(max_length=255, null=True, blank=True)
	password = models.CharField(max_length=255, null=True, blank=True)
	mobile = models.CharField(max_length=50, null=True, blank=True)
