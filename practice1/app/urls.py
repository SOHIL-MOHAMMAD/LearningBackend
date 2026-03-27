from django.urls import path
from . import views

urlpatterns = [
    path('time/',views.date),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact, name='contact'),
    path('name/<str:n>/',views.name, name='name'),
    path('square/<int:num>/', views.Square, name='square'),
    path('quote/', views.randomQuote, name='randomQuote'),
    path('list/', views.Student_list, name='Student_list')
]

