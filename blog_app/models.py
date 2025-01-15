from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)  # 文章標題
    summary = models.TextField()  # 文章摘要
    content = models.TextField()  # 文章內容
    author = models.CharField(max_length=100)  # 作者名稱
    created_at = models.DateTimeField(auto_now_add=True)  # 創建時間
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)  # 預覽圖片

    class Meta:
        db_table = 'article'
