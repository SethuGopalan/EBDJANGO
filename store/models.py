from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255 , unique=True)
class Meta:
    verbose_name_plural = 'categories'

# def get_absolute_url(self):
#     return reverse('store:category_list' , agrs=[self.slug])
def __str__(self):
    return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, related_name= 'product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'images/')
    slug = models.SlugField(max_length=255)
    in_stock= models.BooleanField(default=True)
    is_active= models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class Meta:
    verbose_name_plural = 'Product'
    ordering = ('-created')
def __str__self(self):
    return self.title


