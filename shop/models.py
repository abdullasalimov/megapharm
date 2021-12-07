from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dis_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    category = ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title
