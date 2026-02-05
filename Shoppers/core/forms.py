from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border border-white text-cyan-300 bg-gray-800'

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder':'Your Username',
                'class':INPUT_CLASSES
                }))
    password=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder':'Your password',
                'class':INPUT_CLASSES
                }))
    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder':'Your Username',
                'class':INPUT_CLASSES
                }))
    email=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder':'Your email',
                'class':INPUT_CLASSES
                }))
    password1=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder':'Your password',
                'class':INPUT_CLASSES
                }))
    password2=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder':'Repeat password',
                'class':INPUT_CLASSES
                }))
                                      
