from django.contrib import admin
from .models import Article,ArticleCategory,ArticleComment

# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content','publish_time','category','author']

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'publish_time', 'author', 'article']


admin.site.register(ArticleCategory,ArticleCategoryAdmin)





