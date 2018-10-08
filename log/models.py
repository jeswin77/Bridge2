# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Category(models.Model):
	category_name=models.CharField(max_length=25)
	category_isapproved=models.BooleanField(default=False)


	def __str__(self):
		return self.category_name

class Student(models.Model):
	user_data = models.OneToOneField(User)
	stud_locality = models.CharField(max_length=255)
	
	stud_pic=models.ImageField(upload_to="media/studentpics",blank=True)
	CHOICELIST=Category.objects.all()
	stud_course=models.ForeignKey(Category,on_delete=models.CASCADE)
	

	def __str__(self):
		return self.user_data.first_name





class Tutor(models.Model):
	user_data = models.OneToOneField(User)
	tut_locality = models.CharField(max_length=255,blank=True)
	tut_rate=models.IntegerField(blank=True,null=True)
	tut_rating=models.IntegerField(null=True,blank=True)
	type=(('freelance','Freelance Tutor'),('company','Company'))
	tut_type=models.CharField(max_length=15,choices=type)

	#CHOICELIST=Category.objects.all()
	tut_course=models.ForeignKey(Category,related_name="tutors",default=1)

	tut_pic=models.ImageField(upload_to="media/tutorpics",blank=True,null=True,default='static/unk.png')
	

	tut_upvotes=models.ManyToManyField(User,related_name="ups",blank=True)
	tut_downvotes=models.ManyToManyField(User,related_name="downs",blank=True)

	tut_status=models.CharField(max_length=10,blank=True)



	def __str__(self):
		return self.user_data.username


	def total_likes(self):
		return self.tut_upvotes.count()

	def total_dislikes(self):
		return self.tut_downvotes.count()

	def total_rating(self):
		self.tut_rating=self.total_likes()-self.total_dislikes()
		return self.tut_rating

	def status(self):
		rating=self.total_rating()
		if rating>1000:
			self.tut_status="Platinum"
		elif rating>100 and rating<1000:
			self.tut_status="Gold"
		elif rating<100 and rating>10:
			self.tut_status="Silver"
		else:
			self.tut_status="Bronze"
		return self.tut_status




class StudTutMap(models.Model):
	student=models.ForeignKey(Student)
	tutor=models.ForeignKey(Tutor)
	course=models.ForeignKey(Category)

	def __str__(self):
	 	return '{}-{}'.format(self.tutor.user_data.username,self.student.user_data.username)













