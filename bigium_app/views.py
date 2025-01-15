from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
#reverse_lazy: It is useful for when you need to use a URL reversal before your project’s URLConf is loaded.

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def article_content(request):
    return render(request, template_name="article_content.html")
@login_required(login_url=reverse_lazy("bigium_auth_app:login"))
def write_article(request):
    return render(request,template_name="write_article.html")