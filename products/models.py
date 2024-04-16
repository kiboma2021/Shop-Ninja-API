from django.db import models
from django_extensions.db.fields import AutoSlugField

class Category(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique= True)

    def __str__(self):
        return self.name

class Item(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500, blank= True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name



