from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import ToppingForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

# When a URL request matches the pattern we just defined, 
# Django looks for a function called index() in the views.py file.
# views - bringing in from models and show it on template html file
# but before that you need to add it to url.file creating a url.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'Pizzas/index.html')
@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    #allows you to use template tag, variables in template file 
    context = {'pizzas' : pizzas}
    #load up the page to view
    return render(request, 'Pizzas/pizzas.html', context)
@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.topping_set.order_by('date_added')

    context = {'pizza': pizza, 'toppings':toppings}

    return render(request, 'Pizzas/pizza.html', context)
@login_required
def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    if request.method != 'POST':
        form = ToppingForm() 
    
    else:
        form = ToppingForm(data = request.POST)

        if form.is_valid():
            new_topping = form.save(commit = False)
            new_topping.pizza = pizza
            new_topping.owner = request.user
            new_topping.save()
            
            return redirect('Pizzas:pizza', pizza_id = pizza_id)

    context = {'form': form, 'pizza': pizza}
    return render(request, 'Pizzas/new_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if pizza.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect('Pizzas:pizza',pizza_id=pizza.id)

    context = {'topping':topping, 'pizza':pizza, 'form':form}  
    return render(request, 'Pizzas/edit_.html', context)

@login_required
def new_comment(request, p_id):
    pizza = Pizza.objects.get(id=p_id)

    if request.method != 'POST':
        form = CommentForm()
    
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.owner = request.user
            new_comment.save()
            return redirect('Pizzas:pizza',pizza_id=p_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'Pizzas/new_comment.html', context)




