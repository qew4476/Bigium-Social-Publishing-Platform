from django.urls import path
from . import views

app_name = "bigium_app" # build for pages and article management
urlpatterns = [path('', views.index, name="index"),
               path('article/<int:article_id>', views.article_content, name="article_content"),
               path('write/', views.write_article,name="write_article"),
               path('comment/', views.write_comment, name="write_comment"),
               path('search/', views.search_article, name="search_article"),
               ]