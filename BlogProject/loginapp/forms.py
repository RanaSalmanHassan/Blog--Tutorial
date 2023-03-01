from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)

class Edit_Profile_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)