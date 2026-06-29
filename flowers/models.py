from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Flowers(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250,  unique=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})