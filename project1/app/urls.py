from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home , name='home'  ),
    path('form/',views.home_view,name='home_form'),
    path('modelForm/',views.Model,name ='Model'),
    path('', views.Home_page, name='home_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('validation/', views.validForm, name='validatefrom'),
    
    

]
