from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader 
from . forms import * 
from .models import *
from .filters import *
from django.contrib.auth import authenticate,login  
from django.contrib.auth.decorators import login_required
from django.urls import reverse
   

# Create your views here.
def index(request):
        template = loader.get_template('index.html')
        homeContent = template.render()
        return HttpResponse(homeContent)


def login(request):
        template = loader.get_template('login.html')
        return HttpResponse(template.render())
def dash(request):
        template = loader.get_template('base.html')
        return HttpResponse(template.render())

def payments(request):
        template = loader.get_template('payments.html')
        return HttpResponse(template.render())

def dolls(request):
        template = loader.get_template('dolls.html')
        return HttpResponse(template.render())

def procurement(request):
        template = loader.get_template('procurement.html')
        return HttpResponse(template.render())

def addsitter(request):
    if request.method == 'POST':
        form = Sitterreg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sittersform')
    else:
        form=Sitterreg_form()
    return render(request,'addsitter.html',{'form':form})


def sittersform(request):
      sitters= Sitterreg.objects.all()
      return render(request,'sittersform.html',{'sitters':sitters})

    


def read_sitter(request,id ):
      sitters_info=Sitterreg.objects.get(id=id)
      return render(request,'read_sitter.html',{'sitters_info':sitters_info})

def edit_sitter(request,id):
      sitter=get_object_or_404(Sitterreg,id=id)
      if request.method == 'POST':
            form=Sitterreg_form (request.POST,instance=sitter)
            if form.is_valid():
                  form.save()
                  return redirect('sittersform')
      else:
            form =Sitterreg_form(instance=sitter)
      return render(request,'edit_sitter.html',{'form':form,sitter:sitter})
            
      


def babiesform(request):
      babies= Babyreg.objects.all()
      return render(request,'babiesform.html',{'babies':babies})

def addbaby(request):
    if request.method == 'POST':
        form = Babyreg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('babiesform')
    else:
        form=Babyreg_form()
    return render(request,'addbaby.html',{'form':form})


def read(request,id ):
      babies_info=Babyreg.objects.get(id=id)
      return render(request,'read.html',{'babies_info':babies_info})

def edit(request,id):
      baby=get_object_or_404(Babyreg,id=id)
      if request.method == 'POST':
            form=Babyreg_form (request.POST,instance=baby)
            if form.is_valid():
                  form.save()
                  return redirect('babiesform')
      else:
            form =Babyreg_form(instance=baby)
      return render(request,'edit.html',{'form':form,baby:baby})
            
      











