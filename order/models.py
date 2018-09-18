import decimal
from decimal import Decimal
from django.db import models
from django.urls import reverse

quant = Decimal('0.01')

class Size(models.Model):
	name = models.CharField(max_length=24)
	base_price = models.DecimalField(max_digits=4,decimal_places=2,default=0.00)
	def __str__(self):
		return self.name

class Topping(models.Model):
	name = models.CharField(max_length=24)
	base_price = models.DecimalField(max_digits=4,decimal_places=2,default=1.00)

	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length=64)
	number = models.CharField(max_length=20)
	address = models.CharField(max_length=150)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("root")

class Pizza(models.Model):
	size = models.ForeignKey(Size, null=True, on_delete=models.CASCADE)
	toppings = models.ManyToManyField(Topping)
	#crust = models.ForeignKey(Flavor, null=True, on_delete=models.CASCADE)
	base_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	made_by    = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		if not Pizza.objects.filter(id=self.id):
			super(Pizza, self).save(*args, **kwargs)
		else:
			price = Decimal('0.00')
			if self.size:
				price = self.size.base_price
				print(price)
				for topping in self.toppings.all():
					if topping.base_price:
						price = price + topping.base_price

			self.base_price = decimal.Decimal(str(price)).quantize(quant)
			print(price)
			super(Pizza, self).save(*args, **kwargs)

	def __str__(self):
		if self.size.name:
			name = self.size.name + " Pizza"
		else:
			name = "Pizza"
		for topping in self.toppings.all():
			if topping.name:
				name = name + ", " + topping.name
		return name



class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	date = models.DateField()
	pizzas = models.ManyToManyField(Pizza, blank=True)
	#breads = models.ManyToManyField(Bread, blank=True)
	#is_made = models.BooleanField(default=False)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	is_collected = models.BooleanField(default=False)
	is_delivered = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if not Order.objects.filter(id=self.id):
			super(Order, self).save(*args, **kwargs)
		else:
			decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
			self.subtotal = Decimal('0.00')

			for pizza in self.pizzas.all():
				self.subtotal += pizza.base_price
				for topping in pizza.toppings.all():
					self.subtotal += topping.base_price

				for bread in self.breads.all():
					self.subtotal += bread.base_price

			
			if self.subtotal < 30.00:
				self.total = self.subtotal + 8.00
			self.total = self.total.quantize(quant)
			super(Order, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse("new_customer", kwargs={"pk": self.id})

