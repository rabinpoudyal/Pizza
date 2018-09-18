from django.contrib import admin
from order.models import Size, Topping, Pizza
from order.models import Customer, Order

class OrderAdmin(admin.ModelAdmin):
	def pizza_count(self,obj):
		return obj.pizzas.count()
	def customer_address(self,obj):
		return obj.customer.address
	def customer_phone(self, obj):
		return obj.customer.number
	list_display = ("customer","customer_address","customer_phone", "date", "is_collected", "is_delivered","pizza_count", "subtotal", "total")

class PizzaAdmin(admin.ModelAdmin):
	def toppings_info(self, obj):
		return list(obj.toppings.all())
	list_display = ("size", "toppings_info", "base_price")

#admin.site.register(Flavor)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Pizza, PizzaAdmin)
#admin.site.register(Bread)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)

