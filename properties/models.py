from django.db import models

# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150, default='No description available')
    full_description = models.TextField(max_length=600, default='No description available')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property_images/')
    is_available = models.BooleanField(default=True)
    year_built = models.IntegerField(null=True, blank=True)

     # Image fields
    front_yard = models.ImageField(upload_to='property_images/', null=True, blank=True)
    interior = models.ImageField(upload_to='property_images/', null=True, blank=True)
    backyard = models.ImageField(upload_to='property_images/', null=True, blank=True)



    def __str__(self):
        return self.title


