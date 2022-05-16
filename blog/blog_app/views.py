from django.shortcuts import render
from blog_app.models import Article


def all_articles(request):
    articles = Article.objects.all()
    return render(request, "articles/index.html", {"articles": articles})
