from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CoffeeUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	debt = models.CharField(max_length=100)
	coffees = models.IntegerField()

	def __str__(self):
		return self.user.username + " : " + str(self.debt)

class Coffee(models.Model):
	coffeeuser = models.ForeignKey(CoffeeUser, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.coffeeuser.user.username + " : " + str(self.date)