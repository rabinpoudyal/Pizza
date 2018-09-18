from django.views.generic import CreateView
from order import models
from order.forms import *

class NewOrderView(CreateView):
	model = models.Order
	fields = ("is_delivered", "is_collected", "pizzas")

class NewCustomerView(CreateView):
	model = models.Customer
	#form_class = CustomerForm
	fields = ("name", "number", "address")