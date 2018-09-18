# from django.conf.urls.defaults import *
# from order.views import order_pizza, order_bread

from django.urls import path
from order.views import *


urlpatterns = [
	path('new/', NewOrderView.as_view(), name="new_order"),
	path('<int:pk>/customer/new', NewCustomerView.as_view(), name="new_customer")
]