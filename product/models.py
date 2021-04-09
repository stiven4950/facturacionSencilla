from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(verbose_name='Precio')
    quantity = models.IntegerField(verbose_name='Cantidad')
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        ordering = ['created']

    def __str__(self):
        return self.name
    
    def get_total_item_price(self):
        return self.quantity * self.price

class Order(models.Model):
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    global_price = models.FloatField(default=0)
    start_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']
