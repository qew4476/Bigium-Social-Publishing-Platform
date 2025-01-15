import random
import string

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from .models import CaptchaModel
from .forms import RegisterForm, LoginForm


@require_http_methods(['GET', 'POST'])
def login_form(request):
    """The login Page(html) and the login action"""
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  # POST
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember = form.cleaned_data.get("remember")
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                # Login this user
                login(request, user)

                # verify if the user want to be remembered
                # default: the session will be remembered
                # so it only need to be processed when the user don't want to be remembered.
                if not remember:
                    request.session.set_expiry(0)
                return redirect('/')  # to home page
            else:
                form.add_error('email', 'Email or password error!')
                return render(request, "login.html", context={"form": form})
        else:
            form.add_error('email', 'Email or password error!')
            return render(request, "login.html", context={"form": form})


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:  # POST
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(email=email, username=username, password=password)
            return redirect(reverse('bigium_auth_app:login'))
        else:
            print(form.errors)
            return render(request, 'register.html', {'form': form})


def send_email_captcha(request):
    if request.method == 'POST':
        # get the email for the form
        email = request.POST.get('email')
        # check if email is provided and validate the email format in one step
        try:
            if not email:
                raise ValidationError("email is required")
            validate_email(email)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

        # send the captcha to the email
        captcha = "".join(
            random.sample(string.digits, 4))  # Sampling will get:['2','3','4','8'], so it needs to be joined
        send_mail("Bigium: Captcha Verification Code", f"Your captcha:{captcha}", recipient_list=[email],
                  from_email=None)  # Default from_email has been set up
        # Create a new captcha if not exists, but update if there have been one captcha already.
        CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
        return JsonResponse({"msg": "Captcha has been sent successfully."}, status=200)
