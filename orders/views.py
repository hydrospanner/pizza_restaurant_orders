from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime

from .models import Topping, Order
from .forms import OrderForm


def index(request):
    toppings = Topping.objects.all()
    context = {'toppings': toppings}
    return render(request, 'orders/index.html', context)

def thanks(request):
    return render(request, 'orders/thanks.html')

def place_order(request):
    # check if an unplaced order exists for this user. 
    # if not create a new order and save it. 
    try:
        open_order = Order.objects.get(user=request.user, placed=False)
    except Order.DoesNotExist:
        open_order = Order.objects.create(user=request.user, cost=0.0)
        open_order.save()

    if request.method == 'POST':
        open_order.placed = True
        open_order.cost = open_order.get_cost()
        open_order.added_on = datetime.datetime.now()
        open_order.save()
        return HttpResponseRedirect(reverse("thanks"))
    else:
        form = OrderForm()
        pizzas = open_order.pizzas.all()
        return render(request, 'orders/order.html', {'form': form, 'pizzas': pizzas, 'total': open_order.get_cost()})

def add_pizza(request):
    if request.method == 'POST':
        # get order by searching for user's unplaced order. Return error if not there
        # add pizza to order's pizzas
        pizza_form = OrderForm(request.POST)
        if pizza_form.is_valid():
            pizza = pizza_form.save()
            open_order = Order.objects.get(user=request.user, placed=False)
            open_order.pizzas.add(pizza)
            pizzas = open_order.pizzas.all()
        form = OrderForm()
        return HttpResponseRedirect(reverse("order"))
