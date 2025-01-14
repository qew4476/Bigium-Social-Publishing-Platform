from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def captcha_verification(request):
    pass

#2.
#3. POST 發送驗證碼 (設定env檔)
#4. 寄存到DB
#5.