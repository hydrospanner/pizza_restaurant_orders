from django.test import TestCase, Client

from .models import PizzaCrust, Topping, Pizza
# Create your tests here.

class OrdersTestCase(TestCase):

    def setUp(self):
        top1 = Topping.objects.create(name='pep', cost=1.0)
        top2 = Topping.objects.create(name='basil', cost=1.0)

        crust = PizzaCrust.objects.create(type='pie', size='regular', cost=10.0, topping_cost_factor=1.0)

        pizza1 = Pizza.objects.create(crust=crust, pk=1)
        pizza1.toppings.add(top1, top2)

    def test_topping_cost(self):
        pep = Topping.objects.get(name='pep')
        self.assertEqual(pep.cost, 1.0)

    def test_pizza_cost(self):
        pizza1 = Pizza.objects.get(pk=1)
        self.assertEqual(pizza1.cost(), 12.0)

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['toppings'].count(), 2)