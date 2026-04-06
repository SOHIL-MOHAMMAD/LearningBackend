from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators  import login_required
from .form import InputForm, Form, PostForm



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


# home page
def Home_page(request):
    return render(request, 'page.html')


# register
def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.save()

        return redirect("login")

    return render(request, "register.html")


# login
def login_user(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")


# logout
def logout_user(request):
    logout(request)
    return redirect("home")


# protected page
@login_required
def dashboard(request):
    return render(request, "dashboard.html")


def validForm(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data submitted successfully')
        return render(request,'Validation.html', {'form':form})
    form = PostForm()
    
    return render(request, 'Validation.html',{'form':form})


