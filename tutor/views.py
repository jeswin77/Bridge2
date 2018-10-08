# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from log.models import Category,Tutor
from .models import Advertisement
from .forms import AdForm
from django.shortcuts import redirect,render_to_response

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from tutor.models import TutorNotes
from log.models import Tutor
from django.views.generic import CreateView
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            
        	#cht = Tutor.objects.get(user_data__id=request.user.id)
        	#content=request.POST.get('tut_notes')
        	x = form.save(commit=False)
        	x.tutor = Tutor.objects.get(user_data__id=request.user.id)
        	x.save()
    
        	return HttpResponseRedirect('/profile/')
    else:
        	form = UploadFileForm()
    return render(request, 'tutor/upload.html', {'form': form})

def notes(request):
    tut=TutorNotes.objects.all()
    return render(request,'tutor/notes.html',{'tutnotes':tut})

def search(request):
    pdtl=[]

    template_name='tutor/searchresults.html'
    if request.method == 'GET': # If the form is submitted
        searchresult=0
        search_query = request.GET.get('search_box', None)

        course_selected = request.GET.get('course', None)
        request.session['course']=course_selected
        if course_selected:
            tutors_selected=Tutor.objects.filter(tut_course__category_name__contains=course_selected)
            
            pdtl.append(tutors_selected)
            if tutors_selected:
                searchresult=1
            template_name='tutor/searchresults.html'
            context={'products':tutors_selected}
            return render(request,template_name,context)


    

        if search_query:
            courses=Category.objects.filter(category_name__contains=search_query)
            if courses:
                searchresult=1
            tutors_firstname=Tutor.objects.filter(user_data__first_name__contains=search_query)
            if tutors_firstname:
                searchresult=1
            tutors_lastname=Tutor.objects.filter(user_data__last_name__contains=search_query)
            if tutors_lastname:
                searchresult=1
            notes=TutorNotes.objects.filter(title__contains=search_query)
            if notes:
                searchresult=1
            free=TutorNotes.objects.filter(tut_notes_type__contains=search_query)
            if free:
                searchresult=1
            tutorsatlocality=Tutor.objects.filter(tut_locality__contains=search_query)
            if tutorsatlocality:
                searchresult=1
            context={
            'courses':courses,
            'tutors_firstname':tutors_firstname,
            'tutors_lastname':tutors_lastname,
            'notes':notes,
            'free':free,
            'tutorsatlocality':tutorsatlocality,
            'searchresult':searchresult
            }
            if search_query == 'tutor' or search_query == 'tutors' or search_query =='available tutors' or search_query =='all tutors':
                return redirect('/viewtutors/')    
            


        else:
            context={}
        return render(request,template_name,context)



def ad(request):
    if request.method=='GET':
        context={'form':AdForm}
        return render(request,'tutor/ad.html',context)


    if request.method=='POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.tutor = Tutor.objects.get(user_data__id=request.user.id)
            obj.save()

        else:
            form=AdForm
            
        context={"form":form}
        return redirect('/profile/')
