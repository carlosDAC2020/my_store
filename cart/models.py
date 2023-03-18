import datetime

from django.db import models
from django.utils import timezone

from home.models import Product
from users.models import User

class Invoice(models.Model):
     
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)
    worth_invoice = models.IntegerField(default=0)
    date_invoice = models.DateTimeField(" date invoice ")
    status_payment = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.pk)

    def invoice_most_recently(self):
        return self.date_invoice >= timezone.now() - datetime.timedelta(minutes=30) and self.status_payment==False
        

class Sale(models.Model):# tabla ventas
    # columna             # tpos de datos 
    id_invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units_product = models.IntegerField(default=0)
    worth_sale = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)
