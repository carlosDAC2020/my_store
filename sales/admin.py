from django.contrib import admin
from .models import Invoice,Sale

class InvoiceAdmin(admin.ModelAdmin):
    list_display=["pk","id_client","worth_invoice","date_invoice","status_payment"]
    list_filter=["date_invoice"]

admin.site.register(Invoice, InvoiceAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display=["pk","id_invoice","id_product","units_product","worth_sale"]

admin.site.register(Sale, SaleAdmin)