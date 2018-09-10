from django.db import models

# Create your models here.

class Pizza(models.Model):
    size = models.ForeignKeyField(Size, null=True)
    toppings = models.ManyToManyField(Toppings, null=True)
    curst = models.ForeignKey(Flavor, null=True)
    base_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    def __str__(self):
        if self.size.name:
            name = self.size.name + " Pizza"
        else:
            name = "Pizza"
        for topping in self.toppings.all():
            if topping.name:
                name = name + ", " + topping.name
        return name

class Size(models.Model):
    name = models.CharField(max_length=30)
    base_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name

class Toppings(models.Model):
    name = models.CharField(max_length=30)
    base_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name

class Flavor(models.Model):
    name = models.CharField(max_length=30)
    base_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name

class Bread(models.Model):
    flavor = models.Flavor(Flavor)
    base_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    def __str__(self):
        return self.type

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateTimeField()
    pizzas = models.ManyToManyField(Pizza, null=True)
    breads = models.ManyToManyField(Bread, null=True)
    is_made = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    def __str__(self):
        return str(self.id)

