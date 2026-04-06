# simple form

from django import forms


from .models import FormModel, Post


class InputForm(forms.Form):
  First_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length= 100)
  roll_number = forms.IntegerField(help_text= "enter 6 digit roll number")
  password = forms.CharField(widget= forms.PasswordInput())

  
class Form(forms.ModelForm):
  class Meta:
    model = FormModel
    fields = "__all__"


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields  = ['username','gender','text']
    
    
  def clean(self):
    cleaned_data = super().clean()
    username = cleaned_data.get('username')
    text = cleaned_data.get('text')
    
    if username and len(username) < 5:
      self.add_error('username', 'minimum 5 character required')
    
    if text and len(text) < 10:
      self.add_error('text', 'post should contain atlest 10 character')
      
    return cleaned_data
    
    