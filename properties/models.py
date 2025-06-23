from django.db import models

# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property_images/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


