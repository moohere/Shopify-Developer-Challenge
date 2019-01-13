from django.db import models

# Only one model here: the product. Included the required fields as well as a description field.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    inventory_count = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default="Insert Description Here.")

    def __str__(self):
        return self.title