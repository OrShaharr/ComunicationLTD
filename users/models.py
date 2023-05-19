from typing import Iterable, Optional
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=100, unique=True)
    REQUIRED_FIELDS = ['name', 'email', 'phone']
    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name
    


