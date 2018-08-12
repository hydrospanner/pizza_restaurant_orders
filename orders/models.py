from django.db import models
from django.contrib.auth.models import User
import datetime


class PizzaCrust(models.Model):
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    cost = models.FloatField()
    topping_cost_factor = models.FloatField()

    def __str__(self):
        return f'{self.size} {self.type}'


class Topping(models.Model):
    name = models.CharField(max_length=200)
    cost = models.FloatField()

    def __str__(self):
        return self.name


class Pizza(models.Model):
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)

    def cost(self):
        base_cost = self.crust.cost
        toppings_cost = sum([topping.cost for topping in self.toppings.all()])
        return base_cost + toppings_cost * self.crust.topping_cost_factor

    def __str__(self):
        toppings_s = ', '.join([topping.name for topping in self.toppings.all()])
        return f'{self.crust}: {toppings_s}'


class Special(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    pizzas = models.ManyToManyField(Pizza)
    cost = models.FloatField()

    def __str__(self):
        return self.title


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    cost = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    added_on = models.DateTimeField(auto_now=True, null=True)
    fulfilled = models.BooleanField(default=False)
    placed = models.BooleanField(default=False)

    def get_cost(self):
        return sum([pizza.cost() for pizza in self.pizzas.all()])

    def __str__(self):
        time = self.added_on.strftime('%H:%M:%S')
        return f'{self.user.username} on {time}'
        