from django.db import models
from django.contrib.auth.models import User

class Client(User):
    phone = models.IntegerField(default=0)
    balance = models.IntegerField(default=20000)

    def __str__(self):
        return self.username
    
    def balance_print(self):
        return str(self.balance)