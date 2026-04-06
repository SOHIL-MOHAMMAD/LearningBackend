from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)

class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    
# crud operation   in todo 
class Todo(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)