from django.utils import timezone
from django.db import models

# Choices
BUILDING_CHOICES = [
    ('Main Building', 'Main Building'),
	('Sense Building', 'Sense Building'),
]

TYPE_CHOICES = [
    ('Hiwi', 'Hiwi'),
	('Research Assistant', 'Research Assistant'),
]

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	qr = models.SlugField(max_length=255, unique=True)
	email = models.EmailField(max_length=255)
	type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='Research Assistant')
	building = models.CharField(max_length=255, choices=BUILDING_CHOICES, default='Main Building')
	debth = models.DecimalField(max_digits=6, decimal_places=2)
	coffees = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Coffee(models.Model):
	user = models.ForeignKey(Employee, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	@property
	def today(self):
		return timezone.now().date() == self.date.date()

	class Meta:
		ordering = ["-date"]

	def __str__(self):
		return "Cup added to " + self.user.name + " @ " + str(self.date)