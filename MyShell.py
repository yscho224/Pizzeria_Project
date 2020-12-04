import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()



from Pizzas.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print("Pizza ID:", pizza.id, " Pizza:", pizza)


t = Pizza.objects.get(id = 3)
print(t.name)
print(t.date_added)
