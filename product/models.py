from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000)


    def __str__(self):
        return self.name

