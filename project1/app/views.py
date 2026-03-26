from django.shortcuts import render
from django.http import HttpResponse

from .form import InputForm, Form



# Create your views here.

def home(request):
  return HttpResponse('hello world')
  
# simple form view function

def home_view(request):
  context = {}
  context['form'] = InputForm()
  return render(request, 'form.html', context)



# model form

def Model(request):
  context = {}
  form = Form(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    
  context['form'] = form
  return render(request,'home.html',context)

