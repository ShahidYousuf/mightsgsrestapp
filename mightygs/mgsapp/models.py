# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=200, default="Shahid Yousuf")

	def __unicode__(self):
		return u'%s' % self.name