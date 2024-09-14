from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    quantity = models.IntegerField(default=0)

    # Representasi dari object
    def __str__(self):
        return (self.name + ' - ' + str(self.price) + ' - ' + self.description)