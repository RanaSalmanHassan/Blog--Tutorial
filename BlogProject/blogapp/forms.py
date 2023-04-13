from django import forms
from .models import Blog_Model,Comment
from django.forms import ModelForm, TextInput, EmailInput

class Create_Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog_Model
        exclude = ('author',)

class Create_Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user','blog',)

        widgets = {
            'comment': TextInput(attrs={
                'style': 'border: none; border-bottom:1px solid gray; width:300px;',
                'placeholder': 'Enter Commment',

                })}