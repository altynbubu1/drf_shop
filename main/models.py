from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='product')
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price}"

