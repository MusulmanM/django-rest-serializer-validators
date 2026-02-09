from django.db import models

# Create your models here.



class Mijoz(models.Model):
    name = models.CharField(max_length=155)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255)
    market_name = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    