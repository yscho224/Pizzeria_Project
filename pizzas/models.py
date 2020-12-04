from django.db import models

# Create your models here.

class Pizza(models.Model):
    '''Type of pizzas.'''
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """returns back whatever it is in string method, string representation of model"""
        return self.text

class Topping(models.Model):
    '''Specific types of pizzas'''
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Pizza Toppings"

    def __str__(self):
        """Return a string representation of the topping"""
        return self.name
    