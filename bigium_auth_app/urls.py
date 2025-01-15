from django.urls import path
from . import views

app_name = "bigium_auth_app"
urlpatterns = [path('login/', views.my_login, name="login"),
               path('register/', views.register, name="register"),
               path('send_email_captcha/', views.send_email_captcha, name="send_email_captcha"),
               path('logout/',views.my_logout,name="logout")
               ]
