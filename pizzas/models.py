from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    '''Type of pizzas.'''
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """returns back whatever it is in string method, string representation of model"""
        return self.name

class Topping(models.Model):
    '''Specific types of pizzas and its toppings'''
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        """Return a string representation of the topping"""
        return f"{self.name[:50]}..."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    