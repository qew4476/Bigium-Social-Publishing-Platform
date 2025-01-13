from django.urls import path
from . import views

app_name = "Bigium_app"
urlpatterns = [path('', views.index, name="index"),
               path('article/', views.article_content, name="article_content")]