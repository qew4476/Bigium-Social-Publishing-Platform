from distutils.command.clean import clean

from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required:': "Please input your username",
        'max_length': "Your username must be between 2 and 20 characters in length.",
        'min_length': "Your username must be between 2 and 20 characters in length."
    })
    email = forms.EmailField(error_messages={"required": "Please input your email",
                                             'invalid': "Please input your email address in the format."})
    captcha = forms.CharField(max_length=4, min_length=4)
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

        captcha_model = CaptchaModel.objects.filter(email=email,captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError("The captcha is wrong!")
        captcha_model.delete()  #Verify successfully, it can be deleted
        return captcha