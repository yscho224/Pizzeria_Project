from django.shortcuts import render
from .models import Pizza, Topping
# Create your views here.

# When a URL request matches the pattern we just defined, 
# Django looks for a function called index() in the views.py file.
# views - bringing in from models and show it on template html file
# but before that you need to add it to url.file creating a url.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    #allows you to use template tag, variables in template file 
    context = {'pizzas' : pizzas}
    #load up the page to view
    return render(request, 'Pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')

    context = {'pizza': pizza, 'toppings':toppings}

    return render(request, 'Pizzas/pizza.html', context)

