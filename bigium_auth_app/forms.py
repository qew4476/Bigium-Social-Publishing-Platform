from distutils.command.clean import clean
from os.path import exists

from django import forms
from django.contrib.auth.models import User
from .models import CaptchaModel


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required:': "Please input your username",
        'max_length': "Your username must be between 2 and 20 characters in length.",
        'min_length': "Your username must be between 2 and 20 characters in length."
    })
    email = forms.EmailField(error_messages={"required": "Please input your email",
                                             'invalid': "Please input your email address in the format."})
    captcha = forms.CharField(max_length=4, min_length=4, error_messages={
        "max_length": "Please input 4 digits",
        "min_length": "Please input 4 digits"
    })
    password = forms.CharField(max_length=20, min_length=6, error_messages={
        'required:': "Please input your password",
        'max_length': "Your password must be between 6 and 20 characters in length.",
        'min_length': "Your password must be between 6 and 20 characters in length."

    })

    def clean_email(self):
        """Verify if the email address is already registered"""
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("The email address is already registered")
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')

        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError("The captcha is wrong!")
        captcha_model.delete()  # Verify successfully, it can be deleted
        return captcha

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError("The username is already registered")
        return username


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={"required": "Please input your email",
                                             'invalid': "Please input your email address in the format."})
    password = forms.CharField(max_length=20, min_length=6, error_messages={
        'required:': "Please input your password",
        'max_length': "Your password must be between 6 and 20 characters in length.",
        'min_length': "Your password must be between 6 and 20 characters in length."

    })
    remember = forms.IntegerField(required=False)