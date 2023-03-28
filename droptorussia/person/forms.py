from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-input', 'size': '30', 'rows':'20'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'size': '30', 'rows':'20'}))