import re

import markdown
from django.shortcuts import render, get_object_or_404, redirect

from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()  # 獲取所有文章

    return render(request, template_name="index.html", context={'articles': articles})


def article_content(request):
    return render(request, template_name="article_content.html")


def article_detail(request, article_id):
    # 獲取文章
    article = get_object_or_404(Article, id=article_id)

    # 使用 Markdown 解析內容並啟用 TOC 插件
    md = markdown.Markdown(
        extensions=[
            "fenced_code",  # 支援程式碼塊
            "codehilite",  # 語法高亮
            "tables",  # 支援表格
            "toc"  # 自動生成目錄
        ]
    )
    article_content_html = md.convert(article.content)

    # 取得自動生成的 TOC
    toc_html = md.toc

    # 傳遞 TOC 和文章內容到模板
    return render(request, 'article_detail.html', {
        'article': article,
        'article_content_html': article_content_html,
        'toc_html': toc_html
    })


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        # 從表單中獲取數據
        title = request.POST.get("title")
        content = request.POST.get("content")

        # 更新文章內容
        article.title = title
        article.content = content
        article.save()

        return redirect('blog_app:article_detail', article_id=article.id)

    return render(request, 'edit_article.html', {'article': article})
