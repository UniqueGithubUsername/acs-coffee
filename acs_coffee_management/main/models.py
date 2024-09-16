from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	qr = models.SlugField(max_length=255, blank=True)
	email = models.EmailField(max_length=255)
	debth = models.DecimalField(max_digits=6, decimal_places=2)
	coffees = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name + " : " + str(self.debth)

class ExtendedUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	debt = models.CharField(max_length=100)
	coffees = models.IntegerField()

class Coffee(models.Model):
	user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)