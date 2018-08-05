from django.http import HttpResponse
from django.shortcuts import render

from .models import Topping

# Create your views here.
def index(request):
    toppings = Topping.objects.all()
    context = {'toppings': toppings}
    return render(request, 'orders/index.html', context)
