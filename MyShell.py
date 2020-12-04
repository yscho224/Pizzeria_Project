import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()



from Pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print("Pizza ID:", pizza.id, " Pizza:", pizza)

toppings = t.topping_set.all()
for topping in toppings:
    print(topping)

