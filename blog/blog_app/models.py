from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, primary_key=True)
    content = models.TextField()
    publish_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse("blog_app:article", kwargs={"slug": self.slug})
