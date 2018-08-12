from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Topping, Order
from .forms import OrderForm


def index(request):
    toppings = Topping.objects.all()
    context = {'toppings': toppings}
    return render(request, 'orders/index.html', context)

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        form = OrderForm()
        return render(request, 'orders/order.html', {'form': form})
