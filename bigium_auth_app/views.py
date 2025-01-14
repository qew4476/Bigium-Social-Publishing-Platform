from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def captcha_verification(request):
    pass

#1. 建db
#2. gmail 開啟SMTP
#3. POST 發送驗證碼
#4. 寄存到DB
#5.