from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# class UserForm(UserCreationForm):
    # class Meta:
    #     model=User
    #     fields=['username', 'email', 'password1', 'password2']

class UserForm(forms.Form):

    username=forms.CharField(max_length=50, required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(max_length=50, required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
        validators=[MinLengthValidator(8)]
    )

    confirm=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
        validators=[MinLengthValidator(8)]
    )

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get("username")).exists():
            raise ValidationError("Bu foydalanuvchi ro'yxatdan o'tgan...")
        return self.cleaned_data["username"]



class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
        
