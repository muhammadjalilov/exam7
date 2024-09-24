from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=15)

