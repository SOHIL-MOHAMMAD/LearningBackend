from django.shortcuts import render
from .models import Album, Song, Todo
from .serializer import AlbumSerializer, SongSerializer, TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def album_list(request):
    try:
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def song_list(request):
    try:
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
# crud operation in api   

# create and read all     
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
# read one + update + delete

@api_view(['GET','PUT','DELETE'])
def todo_detail(request, pk):
    todos = Todo.objects.get(id=pk)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todos)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':   
        todos.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        