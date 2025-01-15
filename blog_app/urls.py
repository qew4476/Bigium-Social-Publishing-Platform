from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [path('', views.index, name="index"),
               path('article/', views.article_content, name="article_content"),
               path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # 文章詳細頁
               path('article/edit/<int:article_id>/', views.edit_article, name='edit_article'),

               ]