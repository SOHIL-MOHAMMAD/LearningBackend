from django.urls import path
from . import views

urlpatterns = [
    path('time/',views.date),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact, name='contact'),
    path('name/<str:n>/',views.name, name='name'),
    path('square/<int:num>/', views.Square, name='square'),
    path('quote/', views.randomQuote, name='randomQuote'),
    path('list/', views.Student_list, name='Student_list'),
    path('person',views.Person_List, name='Person_list'),
    path('',views.todo_list,name='todo_list'),
    path('add/',views.add_todo, name='add_todo'),
    path('update/<int:id>/', views.update_todo, name='update_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo')
]

