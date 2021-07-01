from django.db import models
from django.db.models import fields
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ManyToManyField(Category, related_name='products', null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name