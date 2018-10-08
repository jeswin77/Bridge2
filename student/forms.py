from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from log.models import Student,Tutor,User,Category

from .models import Comment

class LikeForm(forms.ModelForm):
	class Meta:
		model=Tutor
		fields=['tut_upvotes','tut_downvotes']

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['stud_locality','stud_pic']

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','email','username']


class UserForm2(UserChangeForm):
	UserChangeForm.password=None

	class Meta:
		model = User
		fields = ['first_name','last_name','email','username']


class TutorForm(forms.ModelForm):
	class Meta:
		model = Tutor
		fields = ['tut_pic','tut_locality','tut_type']


class EditProfileForm(UserChangeForm):
	UserChangeForm.password=None
	class Meta:
		model=User
		fields=['first_name','last_name','email','username']

class EditProfileTutor(UserChangeForm):
	UserChangeForm.password=None
	class Meta:
		model=Tutor
		fields=['tut_locality','tut_rate','tut_type','tut_course','tut_pic']



class EditProfileStudent(UserChangeForm):
	UserChangeForm.password=None
	class Meta:
		model=Student
		fields=['stud_locality','stud_pic']


class CourseForm():
	class Meta:
		model=Tutor
		fields=['tut_course']


class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['content',]
