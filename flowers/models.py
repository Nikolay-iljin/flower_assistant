from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Flowers(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True, db_index=True, default='')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


