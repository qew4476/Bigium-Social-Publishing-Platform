import random
import string
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


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
        captcha = "".join(random.sample(string.digits,4)) #Sampling will get:['2','3','4','8'], so it needs to be joined
        return JsonResponse({"msg":captcha},status=200)
# 2.
# 3. POST 發送驗證碼 (設定env檔)
# 4. 寄存到DB
# 5.
