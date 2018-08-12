from django.contrib import admin

from .models import PizzaCrust, Pizza, Topping, Special, Order


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('pizzas', )
    list_filter = ('placed', 'fulfilled')
    ordering = ['added_on']

admin.site.register(PizzaCrust)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Special)
admin.site.register(Order, OrderAdmin)
