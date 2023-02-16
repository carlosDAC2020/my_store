from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=["pk","name","units_available","worth_unit"]

admin.site.register(Product, ProductAdmin)