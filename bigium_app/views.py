from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse

from .models import ArticleCategory,Article
from .forms import PublishArticleForm


# reverse_lazy: It is useful for when you need to use a URL reversal before your project’s URLConf is loaded.
# Or we can just "/url"
# Or LOGIN_URL = '/auth/login' in setting.py

# Create your views here.
def index(request):
    return render(request, template_name="index.html")


def article_content(request):
    return render(request, template_name="article_content.html")

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
            Article.objects.create(title=title,content=content,category=category_id, author_id=request.user )
            return JsonResponse({"code":200, "message":"Published Article successfully."})
        else:
            print(form.errors)
            return JsonResponse({"code":400, "message": "Form failed!"})



