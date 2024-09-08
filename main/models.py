from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    quantity = models.IntegerField(default=0)

    # Representasi dari object
    def __str__(self):
        return (self.name + ' - ' + str(self.price) + ' - ' + self.description)