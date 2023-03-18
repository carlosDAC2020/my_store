from django.db import models
from django.contrib.auth.models import User

class Client(User):
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
