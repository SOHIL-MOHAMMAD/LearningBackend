from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
from .models import Student
# Create your views here.


def date(request):
  x = datetime.datetime.now()
  return HttpResponse(x)

def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def contact(request):
  return render(request,'contact.html')

def name(request , n):
  user = n
  return render(request,'name.html', {'user': user} )

def Square(request, num):
  square = num * num
  return render(request,'square.html', {'square':square})

def randomQuote(request):
  quotes = ['ghar ki yaar nahi aayi thuje jassi',
    'rehman dakait di hui maut , badi kasainuma hoti hai',
    'hosla endheen badla',
    'nazar aur sabar',
    'darling darling dil kyu toda pilo pilo alam dhud soda',]
  
  rdm = random.choice(quotes)
  return render(request, 'quotes.html', {'rdm': rdm})


def Student_list(request):
  List = Student.objects.all()
  return render(request,'Student.html',{'List': List})