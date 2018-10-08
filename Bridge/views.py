from django.views.generic import TemplateView
from log.models import Tutor,Student,Category
from tutor.forms import subscriberForm
from tutor.models import Subscribers,Advertisement

from django.shortcuts import render,redirect,render_to_response



def Home(request):
    if request.method=='GET':
        last_ads = Advertisement.objects.order_by('-id')[:6]
        context={'form':subscriberForm,'msg':None,'ads':last_ads}
        return render(request,'hm.html',context)


    if request.method=='POST':
        form=subscriberForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Thanks for Subscribing!"

        else:
            form=subscriberForm
            msg=None

        last_ads = Advertisement.objects.order_by('-id')[:6] 
        context={"form":form,'msg':msg,'ads':last_ads}
        return render(request,'hm.html',context)


class Help(TemplateView):
    template_name="help.html"

class about(TemplateView):
    template_name="about.html"

