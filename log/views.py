
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import render,redirect,render_to_response
from django.views.generic import CreateView,FormView,TemplateView,ListView,View
from django.views.generic.edit import UpdateView

from log.models import Student,Tutor,StudTutMap
from log.forms import UserForm,StudentForm,UserForm2,TutorForm,EditProfileForm,EditProfileTutor,EditProfileStudent,CourseForm

from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from PIL import Image
from django.core.files.base import ContentFile
from io import StringIO
from io import BytesIO
from tutor.models import Advertisement


# Create your views here.



class RegisterStudent(FormView):
    template_name = 'register.html'
    form_class = UserForm
    model = User
        
    def get(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = StudentForm()
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

    def post(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = StudentForm(self.request.POST, self.request.FILES)
        if (user_form.is_valid() and cust_form.is_valid()):
            return self.form_valid(user_form, cust_form)
        else:
            return self.form_invalid(user_form, cust_form)
            
    def get_success_url(self, **kwargs):
        return ('success')

    def form_valid(self, user_form, cust_form):
        self.object = user_form.save()
        self.object.is_staff=True
        self.object.save()

        #blog_obj = user_rec(user_data=self.object, user_type=0)
        #blog_obj.save()
        
        cust_obj = cust_form.save(commit=False)
        cust_obj.user_data = self.object

        '''if cust_obj.stud_pic:
          filename=cust_obj.stud_pic
          im = Image.open(cust_obj.stud_pic)
          im.thumbnail((220, 130), Image.ANTIALIAS)
          im.save(im.filename, quality=60)
        #cust_obj.user_type=0'''
        cust_obj.save()

        return redirect('/')

    def form_invalid(self, user_form, cust_form):
      return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

#------------------------------------------------------------------------------------------------------

class RegisterTutor(FormView):
    template_name = 'register.html'
    form_class = UserForm
    model = User
        
    def get(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = TutorForm()
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

    def post(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = TutorForm(self.request.POST, self.request.FILES)
        if (user_form.is_valid() and cust_form.is_valid()):
            return self.form_valid(user_form, cust_form)
        else:
            return self.form_invalid(user_form, cust_form)
            
    def get_success_url(self, **kwargs):
        return ('success')

    def form_valid(self, user_form, cust_form):
        self.object = user_form.save()
        self.object.is_staff=True
        self.object.save()

        #blog_obj = user_rec(user_data=self.object, user_type=1)
        #blog_obj.save()

        cust_obj = cust_form.save(commit=False)
        cust_obj.user_data = self.object
        #cust_obj.user_type=1
        cust_obj.save()

        return redirect('/')

    def form_invalid(self, user_form, cust_form):
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

#-------------------------------------------------------------------------------------------------------
@login_required
def Profile(request):
  ''' stud=request.GET.get('stud')

    map=StudTutMap.objects.filter(student__user_data__username=str(stud)).filter(tutor__user_data__username=request.user)
  
    map.delete()'''
  #obj=Tutor.objects.all()
  u=request.user
  if u.is_superuser:
    return redirect('/admin')
    # context={'user':u}
    # return render(request,'/admin/',context)
  else:
      

    try:
      obj=Tutor.objects.get(user_data__username=u.username)
    except Tutor.DoesNotExist:
      obj = None
    
    if obj:
      a=u.tutor.tut_course
      stud=request.GET.get('stud', None)
      ad=request.GET.get('ad', None)
      if stud:
        map=StudTutMap.objects.filter(student__user_data__username=str(stud)).filter(tutor__user_data__username=request.user)
        map.delete()
      if ad:
        adv=Advertisement.objects.filter(tutor__user_data__username=request.user)
        adv.delete()

      map_obj=StudTutMap.objects.filter(tutor__user_data__id=u.id)
      tut_ads=Advertisement.objects.filter(tutor__user_data__id=u.id)
      context={'user':request.user,'tut':u.tutor,'tut_course':a,'map':map_obj,'ads':tut_ads}
      return render(request,'profile.html',context)
      
    else:
        tut=request.GET.get('tut', None)
        if tut:
          map=StudTutMap.objects.filter(student__user_data__username=request.user).filter(tutor__user_data__username=str(tut))
          map.delete()
        map_obj=StudTutMap.objects.filter(student__user_data__username=str(request.user.username))
        print(map_obj)
        if map_obj:
          context={'user':request.user,'stud':u.student,'map':map_obj}
          return render(request,'profiles.html',context)
        else:
          context={'user':request.user,'stud':u.student}
          return render(request,'profiles.html',context)
      
      
  
      
        


#-------------------------------------------------------------------------------------------------------


class EditProfile(UpdateView):
  template_name = 'editprofile.html'
  model = User
  form_class = UserForm2
  def get(self,request):
    user = request.user
    if user.is_authenticated:
      return super(EditProfile,self).get(self,request)
    else:
      return redirect('/profile/')
  def get_success_url(self):
    return '/profile/'

  def get_object(self, queryset=None):
    return self.request.user

#---------------------------------------------------------------------------
class CourseSelect(CreateView):
  form_class=CourseForm
  template_name="courseselect.html"
  model=Tutor
  success_url="success!!"

#--------------------------------------------------------------------------------------------------------
'''class TutorUpdate(UpdateView):
    model = Tutor
    fields = ['address','tut_rate','tut_type','Course','pic']
    template_name='tutupdate.html'
    def get_object(self,queryset=None):
      return self.request.user
    def get_success_url(self):
      return '/profile/'''
#-----------------------------------------------------------------------------

class TutorUpdate(UpdateView):
  template_name = 'tutupdate.html'
  model = Tutor
  form_class = EditProfileTutor
  def get(self,request):
    user = request.user
    if user.is_authenticated:
      return super(TutorUpdate,self).get(self,request)
    else:
      return redirect('/profile/')
  def get_success_url(self):
    return '/profile/'

  def get_object(self, queryset=None):
    return self.request.user.tutor

#-----------------------------------------------------------------------------
class StudentUpdate(UpdateView):
  template_name = 'tutupdate.html'
  model = Student
  form_class = EditProfileStudent
  def get(self,request):
    user = request.user
    if user.is_authenticated:
      return super(StudentUpdate,self).get(self,request)
    else:
      return redirect('/profile/')
  def get_success_url(self):
    return '/profile/'

  def get_object(self, queryset=None):
    return self.request.user.student


#-----------------------------------------------------------------------------
def ChangePassword(request):
  if request.method=='POST':
    form=PasswordChangeForm(request.user,request.POST)
    if form.is_valid():
      form.save()
      return redirect('/profile')
  else:
    form=PasswordChangeForm(user=request.user)
    context={'form':form}
    return render(request,'changepassword.html',context)

#---------------------------------------------------------------------------------------------------------
'''def password_reset(request,recvr_mail):
  if request.method=='POST':
    form=PasswordChangeForm(request.user,request.POST)
    if form.is_valid():
      form.save()
      return redirect('/profile')
  else:
    form=PasswordChangeForm(user=request.user)
    context={'form':form}
    return render(request,'changepassword.html',context
  template_name="password_reset_form.html"
  body="Follow the link to reset password"
  subject="password reset OTP"
  rm=recvr_mail

  email = EmailMessage('Subject', 'Body', to=[rm])
  email.send()'''

#---------------------------------------------------------------------------------------------------------

class userselect(TemplateView):
  template_name="userselect.html"

#---------------------------------------------------------------------------------------------------------

















def qry(request):
  pdtl=[]
  products = Product.objects.all()
  order = request.GET.get('order','rel') 
  dict1={'price':'pdt_rate','-price':'-pdt_rate','rel':'pdt_rel1'} 
  ord1=dict1[order]# Set 'name' as a default value
  products = products.order_by(ord1)
  for i in products:
    if i.pdt_qty>=1:
      pdtl.append(i)
    else:
      pass

  return render(request, 'wel.html', {'products': pdtl})
    


def ppro(request,expp,tname):
    
    chpt = Product.objects.get(pdt_id=expp)
    current_user= request.user

    need_qty=request.POST.get('quantity')

    if need_qty:
      request.session['nq']=need_qty
    else:
      pass

    context={'pt':chpt,'user':current_user}
    #return render(request,tname,context)
    return render(tname, context)

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

