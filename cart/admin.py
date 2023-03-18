from django.contrib import admin
from .models import Invoice, Sale

admin.site.register(Invoice)

admin.site.register(Sale)