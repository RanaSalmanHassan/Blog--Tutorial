from django import forms
from .models import Blog_Model

class Create_Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog_Model
        exclude = ('author',)