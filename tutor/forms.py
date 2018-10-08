from django import forms
from tutor.models import TutorNotes,Subscribers,Advertisement

class UploadFileForm(forms.ModelForm):
    #title = forms.CharField(max_length=50)
    #file = forms.FileField()
    class Meta:
    	model=TutorNotes
    	fields=['title','tut_notes','tut_notes_type']

class subscriberForm(forms.ModelForm):
	email= forms.CharField(label='email', 
                    widget=forms.TextInput(attrs={'placeholder': 'your email address'}))
	class Meta:
		model=Subscribers
		fields=['email',]

class AdForm(forms.ModelForm):
	class Meta:
		model=Advertisement
		fields=['ad_title','ad_desc','ad_pic']
