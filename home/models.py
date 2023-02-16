from django.db import models

class Product(models.Model):# tabla productos 
    
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    units_available = models.IntegerField(default=0)
    worth_unit = models.IntegerField(default=0)
    product_photo = models.ImageField(upload_to="products/images")


    def __str__(self):
        return self.name 

    def valid_worth(self):
        if self.worth_unit<0:
            return True

    def valid_units_available(self):
        if self.units_available<0:
            return True
