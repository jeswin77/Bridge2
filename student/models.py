# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from log.models import Tutor,Category
from django.contrib.auth.models import User

class Comment(models.Model):
	tutor=models.ForeignKey(Tutor)
	user=models.ForeignKey(User)
	content=models.TextField(max_length=250)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}-{}'.format(self.tutor.user_data.username,str(self.user.username))



		

