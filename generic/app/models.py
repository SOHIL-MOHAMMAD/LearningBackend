from django.db import models

# Create your models here.


class Student(models.Model):
  
  COURSE_CHOICE =[
    ('BTECH','Btech'),
    ('BCA','BCA'),
    ('MCA','MCA')
  ]
  
  name = models.CharField( max_length=100)
  roll_no = models.IntegerField(unique=True)
  email = models.EmailField(unique=True)
  course = models.CharField(max_length=10, choices=COURSE_CHOICE)
  
  def __str__(self):
    return f"{self.name} ({self.roll_no})"  