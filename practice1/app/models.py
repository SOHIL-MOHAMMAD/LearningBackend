from django.db import models

# Create your models here.


class Student(models.Model):
  first_name = models.CharField( max_length=50)
  last_name = models.CharField( max_length=50)
  age = models.IntegerField()
  degree = models.CharField( max_length=50)
  

class Person(models.Model):
  name = models.CharField( max_length=50)
  age = models.IntegerField()
  
  def __str__(self):
    return f"{self.name} {self.age}"
  
  
class TODO(models.Model):
  title = models.CharField( max_length=200)
  complete = models.BooleanField( default=False)
  
  def __str__(self):
    return self.title