import re

import markdown
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from .models import Article, Tag


# Create your views here.
def index(request):
    tag_id = request.GET.get('tag')  # 獲取標籤 ID
    articles = Article.objects.all().order_by('-created_at')

    if tag_id:
        articles = articles.filter(tags__id=tag_id)  # 過濾包含該標籤的文章

    tags = Tag.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    max_page = paginator.num_pages

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('partials/article_list.html', {'page_obj': page_obj})
        return JsonResponse({'html': html})

    return render(request, 'index.html', {'page_obj': page_obj, 'tags': tags, 'max_page': max_page})

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
    tags = Tag.objects.all()  # 獲取所有標籤

    if request.method == "POST":
        # 從表單中獲取數據
        title = request.POST.get("title")
        content = request.POST.get("content")
        selected_tags = request.POST.getlist("tags")  # 獲取選中的標籤

        # 更新文章內容
        article.title = title
        article.content = content
        article.save()

        # 更新文章的標籤
        article.tags.set(selected_tags)  # 更新標籤

        return redirect('blog_app:article_detail', article_id=article.id)

    return render(request, 'edit_article.html', {'article': article, 'tags': tags})
