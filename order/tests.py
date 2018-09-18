import unittest
import datetime
from django.conf import settings
from django.test.client import Client
from order.models import Order, Customer, Pizza, Bread, Topping
from order.views import place_order, order_pizza
from django.test.utils import setup_test_environment

setup_test_environment()

"""
Model tests

"""

class OrderTestCase(unittest.TestCase):
    def setUp(self):
	self.customer = Customer.objects.create(name='Jim')
	self.order = Order.objects.create(customer=self.customer,
					date = datetime.datetime.now())

    def test_order(self):
	self.assertEqual(self.order.customer.name, 'Jim',
			'customer name incorrect')

    def tearDown(self):
	self.order.delete()
	self.customer.delete()

class PizzaTestCase(unittest.TestCase):
    def setUp(self):
	self.pepperoni = Topping.objects.create(name='Pepperoni')
	self.sausage = Topping.objects.create(name='Sausage')
	self.pizza = Pizza.objects.create(size='M', crust='GR')
	self.pizza.toppings.add(self.pepperoni, self.sausage)

    def test_size(self):
	self.assertEqual(self.pizza.size, 'M',
			"Size not added correctly.")
    def test_toppings(self):
	toppings = self.pizza.toppings.all()
	self.assertEqual(toppings[0].name, 'Pepperoni',
			"Pepperoni not added correctly.")
	self.assertEqual(toppings[1].name, 'Sausage',
			"Sausage not added correctly.")

    def test_crust(self):
	self.assertEqual(self.pizza.crust, 'GR',
			"Crust not added correctly.")

    def tearDown(self):
	self.pizza.delete()
	self.pepperoni.delete()

class BreadTestCase(unittest.TestCase):
    def setUp(self):
	self.bread = Bread.objects.create(type='GR')

    def test_type(self):
	self.assertEqual(self.bread.type, 'GR',
			"Bread type incorrect.")

    def test_price(self):
	self.assertEqual(self.bread.base_price, 4.00,
			"Bread price incorrect.")

    def tearDown(self):
	self.bread.delete()

"""

View tests

"""

class OrderPizzaTestCase(unittest.TestCase):
    fixtures = ['order_order', 'order_pizza']
    def setUp(self):
	client = Client()
	self.response = client.get('/order/', follow=True)

    def test_order(self):
	order = self.response.order.all()[0]
	pizza = order.pizzas.all()[0]
	toppings = pizza.toppings.all()
	self.assertEqual(pizza.size, 'M',
			"Pizza size incorrect on order 1.")
	self.assertEqual(toppings[0].name, 'Pepperoni',
			"Pepperoni not on pizza, order 1")
	self.assertEqual(toppings[1].name, 'Bacon',
			"Bacon not on pizza, order 1")

