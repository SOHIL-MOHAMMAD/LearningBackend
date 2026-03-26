from django.db import models

# Create your models here.


class Member(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=50)
  age = models.IntegerField()
  
  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.age}"
  
  
class FormModel(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  last_modified = models.DateTimeField( auto_now_add=True)
  
  def __str__(self):
    return self.title
