# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import render,redirect,render_to_response
from django.views.generic import CreateView,FormView,TemplateView,ListView,View

from log.models import Tutor,Category,Student,StudTutMap
#from pdt.forms import pdtform,UserForm,CustomerForm,CatgForm
from student.forms import LikeForm,CommentForm
from .models import Comment

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect





# Create your views here.


def qry(request):
  pdtl=[]
  course_list=[]
  products = Tutor.objects.all()
  order = request.GET.get('order','rel') #'rel' is the default parameter for sorting
  
  
  dict1={'rate':'tut_rate','rel':'-tut_rate','rating':'-tut_rating'} 
  ord1=dict1[order]# Set 'name' as a default value
  objs=products.order_by(ord1)
  for i in objs:
  	pdtl.append(i)



  return render(request, 'student/sort.html', {'products': pdtl})
    
#---------------------------------------------------------------------------------------

def ppro(request,expp,is_liked=False,is_disliked=False):
    
    chpt = Tutor.objects.get(user_data__id=expp)
    current_user= request.user

    comment=Comment.objects.filter(tutor=chpt).order_by('-id')

    if request.method=='POST':
      comment_form=CommentForm(request.POST or None)
      if comment_form.is_valid():
        content=request.POST.get('content')
        a=Comment.objects.filter(tutor=chpt,user=request.user,content=content)
        if a.exists():
          pass
        else:
          c=Comment.objects.create(tutor=chpt,user=request.user,content=content)
          c.save()
      else:
        comment_form=CommentForm

    context={'i':chpt,
            'user':current_user,
            "total_likes":chpt.total_likes(),
            "total_dislikes":chpt.total_dislikes(),
            'comment':comment,
            "is_liked":is_liked,
            "is_disliked":is_disliked,
            "comment_form":CommentForm,
            "rating":chpt.total_rating(),
            "status":chpt.status()
            }


    #return render(request,tname,context)


    


    
    return render(request,"student/tutorprofile.html", context)



#-----------------------------------------------------------------------------------------------------------------------

def ppro1(request,expp,tname):
  if "nq" in request.session:
    result = request.session["nq"]
  else:
    result = False
  if result:
    need_quantity=request.session.get('nq')
  
  chpt = Product.objects.get(pdt_id=expp)
  chpt.pdt_qty-=int(need_quantity)

  current_user= request.user
  current_userid= request.user.id


  obj = pdtcustmap.objects.create(cus_id=current_userid,cpdt_id=chpt.pdt_id,cus_name=str(current_user.username))
  

  chpt.save()
    
    

  context={'pt':chpt,'user':current_user}
  return render(request,tname,context)

#--------------------------------------------------------------------------------------------------------------------------

class upage(View):
    def get(self,request,tname):
        current_user=request.user
        context={'user':current_user}
        return render(request,tname,context)

#-------------------------------------------------------------------------------------------

def like_tutor(request):
  l=request.POST.get('tutor_id')
  tut=Tutor.objects.get(id=int(l))

  if tut.tut_upvotes.filter(id=request.user.id).exists():
      tut.tut_upvotes.remove(request.user)
      
      tut.save()
      is_liked=False
  else:
    tut.tut_upvotes.add(request.user)
    
    tut.save()
    is_liked=True

 
  k=str(tut.user_data.id)
  
  return redirect("/tutorprofile/"+k,is_liked=is_liked)

#----------------------------------------------------------------------------

def dislike_tutor(request):
  l=request.POST.get('tutor_id')

 
  tut=Tutor.objects.get(id=int(l))

  if tut.tut_downvotes.filter(id=request.user.id).exists():
      tut.tut_downvotes.remove(request.user)
     
      tut.save()
      is_disliked=False
  else:
    tut.tut_downvotes.add(request.user)
    
    tut.save()
    is_disliked=True

  k=str(tut.user_data.id)
  return redirect("/tutorprofile/"+k,is_disliked=is_disliked)


#-----------------------------------------------------------------------------

def connect_to_tutor(request):
  l=request.POST.get('tutor_id')
  c=request.POST.get('course')
  print(l,"*****************************")
  if request.user.is_superuser:
    tut=Tutor.objects.get(id=int(l))
    k=str(tut.user_data.id)
    return redirect("/tutorprofile/"+k)
    
  else:
    tut=Tutor.objects.get(id=int(l))
    stud=Student.objects.get(user_data__id=request.user.id)
    course=Category.objects.get(category_name=str(c))
    
    map_check=StudTutMap.objects.filter(tutor=tut,student=stud,course=course)
    if map_check:
      k=str(tut.user_data.id)
      return redirect("/tutorprofile/"+k)
    else:
      mapper=StudTutMap.objects.create(tutor=tut,student=stud,course=course)
      k=str(tut.user_data.id)
      return redirect("/tutorprofile/"+k)

