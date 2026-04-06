from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from app.serializer import PRoductSerializer , OrderSerializer, OrderItemSerializer
from .models import Product, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def product_list(request):
  products = Product.objects.all()
  serializer = PRoductSerializer(products, many=True)
  
  return Response(serializer.data)
  
#   return JsonResponse({
#     'data':  serializer.data
# })

  
@api_view(['GET'])
def product_Detail(request, pk):
  product = get_object_or_404(Product, pk=pk)
  serializer = PRoductSerializer(product)
  
  return Response(serializer.data)
  
  
  
@api_view(['GET'])
def order_list(request):
  order = Order.objects.all()
  serializer = OrderSerializer(order, many = True)
  
  return Response(serializer.data)