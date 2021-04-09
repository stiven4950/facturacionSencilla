# predefined packages
from django.urls import path

# custom packages
from .views import OrderSummaryView, add_product, remove_product, remove_one_product, add_one_product, OrderDetailView, generate_order

product_patterns = ([
    path("order/", OrderSummaryView.as_view(), name="order"),
    path("add/", add_product, name="add"),
    path('remove/<int:pk>/', remove_product, name="remove"),
    path('remove-one/<int:pk>/', remove_one_product, name="removeone"),
    path('add-one/<int:pk>/', add_one_product, name="addone"),
    path('generate-order', generate_order, name="generate"),
    path("order-detail/<int:pk>/", OrderDetailView.as_view(), name="orderdetail"),
], 'product')
