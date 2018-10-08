# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from log.models import Tutor

# Create your models here.

class TutorNotes(models.Model):
	tutor=models.ForeignKey(Tutor)
	tut_notes=models.FileField(upload_to='media/TutorNotes',max_length=4000,blank=True)
	notes_type=(('paid','Paid'),('free','Free'))
	tut_notes_type=models.CharField(max_length=15,choices=notes_type)
	timestamp=models.DateTimeField(auto_now_add=True)
	title=models.CharField(max_length=40)

	def __str__(self):
		return self.tutor.user_data.username


class Subscribers(models.Model):
	email=models.CharField(max_length=50)
	def __str__(self):
		return self.email


class Advertisement(models.Model):
	tutor=models.ForeignKey(Tutor)
	ad_title=models.CharField(max_length=25)
	ad_desc=models.CharField(max_length=200)
	ad_pic=models.ImageField(upload_to="media/ads")


	def __str__(self):
		return self.ad_title		





		

