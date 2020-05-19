from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("product",views.product),
    path("add_to_cart",views.add_to_cart),
    path("cart",views.cart),
    path("delete",views.item_delete)
]
