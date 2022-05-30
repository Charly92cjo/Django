from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)#heredar los atributos de un modelo
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=240)#ImageFiled es recomendable para googleCloud, netlify

    def __str__(self):
        return self.name


class Category(models.Model):#relacion entre Productos y categorias, para despues filtrar
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name="categories")#relaciones de muchos a muchos

    def __str__(self):
        return self.name


#luego ir a admin.py
# from django.contrib import admin
# from .models import Product
# from .models import Category

# admin.site.register(Product)
# admin.site.register(Category)