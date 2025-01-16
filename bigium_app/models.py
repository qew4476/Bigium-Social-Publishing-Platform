from django.contrib.auth.models import User
from django.db import models


class ArticleCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ArticleComment(models.Model):
    """Comment to the specific article(foreign key)"""
    comment = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment