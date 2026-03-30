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
  
  