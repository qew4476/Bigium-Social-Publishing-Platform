from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def article_content(request):
    return render(request, template_name="article_content.html")

def write_article(request):
    return render(request,template_name="write_article.html")