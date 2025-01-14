from django.urls import path
from . import views

app_name = "Bigium_app" # build for pages and article management
urlpatterns = [path('', views.index, name="index"),
               path('article/', views.article_content, name="article_content"),
               path('write/', views.write_article,name="write_article")]