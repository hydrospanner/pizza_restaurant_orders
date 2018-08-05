from django.contrib import admin

from .models import PizzaCrust, Pizza, Topping, Special, Order
# Register your models here.


admin.site.register(PizzaCrust)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Special)
admin.site.register(Order)
