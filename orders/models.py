from django.db import models

# Create your models here.

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

