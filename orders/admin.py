from django.contrib import admin

from .models import PizzaCrust, Pizza, Topping, Special, Order


class PizzasInline(admin.StackedInline):
    model = Order.pizzas.through
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    exclude = ('pizzas', )
    list_filter = ('placed', 'fulfilled')
    ordering = ['added_on']
    inlines = [PizzasInline]

admin.site.register(PizzaCrust)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Special)
admin.site.register(Order, OrderAdmin)
