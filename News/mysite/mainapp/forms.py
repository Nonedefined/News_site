from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username',  widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Password confirmation',  widget=forms.PasswordInput(attrs={"class": "form-control"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',  widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = News
        fields = ["title", "content", "category", "photo"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class CommentForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control",
                                                            "rows": 4,
                                                            "placeholder": "What is your view?"}))

