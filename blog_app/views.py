from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def article_content(request):
    return render(request, template_name="article_content.html")


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article_detail.html', {'article': article})