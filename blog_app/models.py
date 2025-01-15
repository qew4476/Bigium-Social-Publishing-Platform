from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 標籤名稱

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'article_tag'


class Article(models.Model):
    title = models.CharField(max_length=255)  # 文章標題
    summary = models.TextField()  # 文章摘要
    content = models.TextField()  # 文章內容
    author = models.CharField(max_length=100)  # 作者名稱
    created_at = models.DateTimeField(auto_now_add=True)  # 創建時間
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)  # 預覽圖片
    tags = models.ManyToManyField(Tag, related_name='articles', through='ArticleWithTagMapping', blank=True)

    class Meta:
        db_table = 'article'


class ArticleWithTagMapping(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'article_with_tag_mapping'  # 自定義中介表名稱
        unique_together = ('article', 'tag')  # 確保每個標籤只會出現一次
