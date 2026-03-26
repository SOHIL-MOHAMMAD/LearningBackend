from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'  ),
    path('form/',views.home_view,name='home_form')
]
