from django.urls import path
from blog_app import views

app_name = "blog_app"

urlpatterns = [
    path("", views.all_articles, name="all"),
    path("<str:slug>/", views.article, name="article"),
]
