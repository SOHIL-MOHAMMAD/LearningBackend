from django.shortcuts import render
from django.http import HttpResponse
from .form import InputForm
# Create your views here.

def home(request):
  return HttpResponse('hello world')
  
# simple form view function

def home_view(request):
  context = {}
  context['form'] = InputForm()
  return render(request, 'form.html', context)