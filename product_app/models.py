from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField(max_length=100)
    make_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
