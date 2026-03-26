from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'  ),
    path('modelForm',views.Model,name ='Model')
]
