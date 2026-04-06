from .models import Album, Song, Todo
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = ['id','title','artist']
    
    
class SongSerializer(serializers.ModelSerializer):
  album = AlbumSerializer(read_only=True)
  class Meta:
    model = Song
    fields = ['id','title','album']
    
# crud operation in api  
class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = '__all__'
    
