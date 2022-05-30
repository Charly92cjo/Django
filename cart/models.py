from django.db import models
from products.models import Product

# Create your models here.
class Cart(models.Model):
    pass#relacion 1 a 1 con el usuario

class CartItem(models.Model):
    amount = models.IntegerField()#cantidad de productos
    product = models.ForeignKey(Product, on_delete=models.CASCADE)#borrar el producto despues
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)