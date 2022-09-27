 
from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.location_name)

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    price = models.FloatField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

image_type = (
    ('Bedroom','Bedroom'),
    ('Bathroom','Bathroom'),
    ('LivingRoom','LivingRoom'),
    ('Reausturant','Reausturant'),
)

# category table contain category image and it's type  
class Category(models.Model):
    image = models.ImageField(upload_to='images')
    type = models.CharField(
        choices= image_type,
        max_length= 100,
        default='Bedroom',
    )
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)