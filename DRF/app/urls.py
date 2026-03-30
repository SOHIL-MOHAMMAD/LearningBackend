from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_Detail, name='product_detail'),
]
