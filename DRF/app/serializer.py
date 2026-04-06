from rest_framework import serializers
from .models import Product, Order, OrderItem

class PRoductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'id',
      'name',
      'description',
      'price',
      'stock',
      
    )
# validating serializer data
  def validate_price(self, value):
    if value <=0:
      raise serializers.ValidationError(
        'Price must be greater than zero'
      )
    return value
  
class OrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderItem
    fields = (
      'order',
      'product',
      'quantity'
    )
  
class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True,read_only=True)
  class Meta:
    model = Order
    fields =(
      'order_id',
      'create_at',
      'user',
      'status',
      'items'
    )