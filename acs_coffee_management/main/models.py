from django.utils import timezone
from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	qr = models.SlugField(max_length=255, unique=True)
	email = models.EmailField(max_length=255)
	debth = models.DecimalField(max_digits=6, decimal_places=2)
	coffees = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name + " : " + str(self.debth)

class Coffee(models.Model):
	user = models.ForeignKey(Employee, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	@property
	def today(self):
		return timezone.now() >= self.date

	class Meta:
		ordering = ["-date"]