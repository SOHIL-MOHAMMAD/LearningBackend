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


class Post(models.Model):
  MALE = 'M'
  FEMALE = 'F'
  GENDER_CHOICE =[
    (MALE,'Male'),
    (FEMALE, 'Female'),
  ]
  
  username = models.CharField( max_length=50, blank=False, null=False)
  text = models.TextField(blank=False, null=False)
  gender = models.CharField( max_length=6, choices= GENDER_CHOICE, default=MALE)
  time = models.DateField( auto_now_add=True)
  
  def __str__(self):
    return self.username