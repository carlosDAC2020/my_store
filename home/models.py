from django.db import models

class Product(models.Model):# tabla productos 
    
    name = models.CharField(max_length=20, default=" ")
    description = models.TextField( default=" ")
    measures = models.CharField(max_length=50, default=" ")
    category = models.CharField(max_length=20, default=" ")
    units_available = models.IntegerField(default=0)
    worth_unit = models.IntegerField(default=0)
    product_photo = models.ImageField(upload_to="products/images")


    def __str__(self):
        return self.name 

    def valid_worth(self):
        if self.worth_unit<1:
            self.worth_unit=0

    def valid_units_available(self):
        if self.units_available<0:
            self.units_available=0
