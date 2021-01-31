from django.shortcuts import render

from .models import Pizza, Topping

# Create your views here.

def index_view(request):
    return render(request, 'pizzas/index.html') 

def list_view(request):
    pizzas=Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)   

def detail_view(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/detail.html', context)
