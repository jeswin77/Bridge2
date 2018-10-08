from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from log.models import Student,Tutor,User,Category



class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['stud_locality','stud_pic','stud_course']

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
		fields = ['tut_pic','tut_locality','tut_type','tut_course']


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
		fields=['stud_locality','stud_pic','stud_course']


class CourseForm():
	class Meta:
		model=Tutor
		fields=['tut_course']




