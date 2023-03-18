from django.urls import path
from . import views

app_name="cart"

urlpatterns = [
    path("", views.my_cart, name="cart"),
    path("<int:product_id>/add_sales/", views.add_sales, name="add_sales"),
    path("<int:id_sale>/delete_sale/", views.delete_sales, name="delete_sale"),
]