from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    short_content = models.TextField(max_length=400, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    news = models.ForeignKey(News, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}, {self.news.title}"


class WeatherCity(models.Model):
    title = models.CharField(max_length=150)
    slug_title = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

