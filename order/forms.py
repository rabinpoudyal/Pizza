from django import forms
from order.models import Pizza,  Customer

class PizzaForm(forms.ModelForm):
	class Meta:
		model = Pizza
		fields = ('size', 'toppings')
		widgets = {
			'size': forms.RadioSelect(),
			'toppings': forms.CheckboxSelectMultiple(),
		}

	def process(self, order):
		data = self.cleaned_data
		size = data['size']
		toppings = data['toppings']

		pizza = Pizza.objects.create()
		pizza.size = size
		pizza.base_price = pizza.size.base_price
		for topping in toppings:
			pizza.toppings.add(topping)
			pizza.base_price += pizza.topping.base_price
		pizza.save()

		order.pizzas.add(pizza)
		order.save()

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ("name","number", "address")

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
													'class': 'form-control'
		})

	def process(self, order):
		data = self.cleaned_data
		name = str(data['name'])
		number = str(data['number'])
		address = str(data['address'])
		customer = Customer.objects.create(name=name, number=number)
		order.customer = customer
		order.save()

