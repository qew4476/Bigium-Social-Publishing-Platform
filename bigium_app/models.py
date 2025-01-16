from django.contrib.auth.models import User
from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=200)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class ArticleComment(models.Model):
    """Comment to the specific article(foreign key)"""
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
