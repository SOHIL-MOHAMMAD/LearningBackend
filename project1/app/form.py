# simple form

from django import forms
from .models import FormModel


class InputForm(forms.Form):
  First_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length= 100)
  roll_number = forms.IntegerField(help_text= "enter 6 digit roll number")
  password = forms.CharField(widget= forms.PasswordInput())
  
  
class Form(forms.ModelForm):
  class Meta:
    model = FormModel
    fields = "__all__"