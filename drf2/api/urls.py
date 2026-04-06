from django.urls import path
from . import views

urlpatterns = [
    path('album/',views.album_list,name='album-list'),
    path('song/', views.song_list, name='song-list'),
    path('todo/',views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_details'),
]
