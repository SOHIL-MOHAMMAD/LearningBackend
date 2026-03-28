from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import datetime
import random
from .models import Student, Person, TODO
from .form import TodoForm
# Create your views here.


def date(request):
  x = datetime.datetime.now()
  return HttpResponse(x)

def home(request):
  title = 'ye hai home page'
  return render(request,'home.html', {'title': title})

def about(request):
  title = 'ye hai about page'
  return render(request,'about.html', {'title':title})

def contact(request):
  title = 'ye hai contact page'
  return render(request,'contact.html',{'title':title})

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
  return render(request,'Student.html', {'List': List})


def Person_List(request):
  title = 'person list with the age of grater than 18'
  List = Person.objects.all()
  return render(request,'person.html',{'List':List ,'title':title})

# read
def todo_list(request):
  todos = TODO.objects.all()
  return render(request, 'todo/list.html', {'todos': todos})

# create
def add_todo(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('todo_list')
    
  else:
    form = TodoForm()
  return render(request,'todo/form.html',{'form':form})


# update

def update_todo(request, id):
  todo = get_object_or_404(TODO, id=id )
  
  if request.method == 'POST':
    form = TodoForm(request.POST, instance= todo)
    if form.is_valid():
      form.save()
      return redirect('todo_list')
  else:
    form = TodoForm(instance=todo)
    
  return render(request , 'todo/form.html', {'form': form})

def delete_todo(request, id):
  todo = get_object_or_404(TODO, id=id)
  todo.delete()
  return redirect('todo_list')


  
  