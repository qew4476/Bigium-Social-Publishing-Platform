from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods,require_POST
from django.http.response import JsonResponse

from .models import ArticleCategory,Article,ArticleComment
from .forms import PublishArticleForm


# reverse_lazy: It is useful for when you need to use a URL reversal before your project’s URLConf is loaded.
# Or we can just "/url"
# Or LOGIN_URL = '/auth/login' in setting.py

# Create your views here.
def index(request):
    return render(request, template_name="index.html")


def article_content(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Exception as e:
        article = None
    return render(request, template_name="article_content.html", context={'article': article})

@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy("bigium_auth_app:login"))
def write_article(request):
    if request.method == "GET":
        categories = ArticleCategory.objects.all()
        return render(request, template_name="write_article.html",context={"categories":categories})
    else:   #POST
        form = PublishArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            category_id = form.cleaned_data.get("category")
            article = Article.objects.create(title=title,content=content,category_id=category_id, author_id=request.user.id )
            return JsonResponse({"code":200, "message":"Published Article successfully.","data":{"article_id":article.id}})
        else:
            print(form.errors)
            return JsonResponse({"code":400, "message": "Form failed!"})

@require_POST
@login_required(login_url=reverse_lazy("bigium_auth_app:login"))
def write_comment(request):
    article_id = request.POST.get("article_id")   # get the article to be reviewed
    comment = request.POST.get("comment")
    article = Article.objects.get(pk=article_id)
    ArticleComment.objects.create(comment=comment, article_id=article, author=request.user)
    #reload
    print(article)
    print(request.user)
    return redirect(reverse("bigium_app:article_content", kwargs={"article_id":article_id}))


