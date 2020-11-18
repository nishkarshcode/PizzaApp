from django.db import models

# Create your models here.
class Toppings(models.Model):
    """This class created for the Pizza Toppings"""
    name                = models.CharField(max_length=150,unique=True,blank=True)
    updated_at          = models.DateTimeField(auto_now=True)
    created_at          = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return self.name
    
PIZZA_TYPES = (
    ('regular','Regular'),
    ('square','Square')
)
PIZZA_SIZES = (
    ('small','Small'),
    ('medium','Medium'),
    ('large','Large'),
)
class Pizza(models.Model):
    name                = models.CharField(max_length=120)
    pizza_type          = models.CharField(max_length=20,choices=PIZZA_TYPES,default='regular')
    sizes               = models.CharField(max_length=20,choices=PIZZA_SIZES,default='small')
    toppings            = models.ManyToManyField(Toppings) 
    updated_at          = models.DateTimeField(auto_now=True)
    created_at          = models.DateTimeField(auto_now_add=True)


