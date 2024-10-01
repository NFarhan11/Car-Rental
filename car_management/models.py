from django.db import models

# Create your models here.
class Car(models.Model):
	brand = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	rental_price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
	availability = models.BooleanField(default=True)
	image = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Storing car images in 'car_images/'

	def __str__(self) -> str:
		return f"{self.brand} {self.model} - ${self.rental_price_per_day}/day"
