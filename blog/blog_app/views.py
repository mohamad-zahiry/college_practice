from django.shortcuts import render
from blog_app.models import Article


def all_articles(request):
    articles = Article.objects.all()
    return render(request, "articles/index.html", {"articles": articles})


def article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/detail.html", {"article": article})
