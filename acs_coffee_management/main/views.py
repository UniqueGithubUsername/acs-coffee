import datetime
import pandas as pd

from django.shortcuts import redirect, render
from django.core.mail import send_mail, send_mass_mail

from .models import Employee

# Create your views here.
def index(request):
	# Get employees
	employees = Employee.objects.all()

	context = {'employees':employees}

	return render(request, 'main/index.html', context)

def export(request):
	# Get employees
	employees = Employee.objects.all()

	# Save as .csv
	df = pd.DataFrame(o.__dict__ for o in employees)
	df.to_csv(str(datetime.date.today()) + "_employees.csv")

	context = {'employees':employees, 'output':"Successfully exported " + str(datetime.date.today()) + "_employees.csv"}

	return render(request, 'main/index.html', context)

def broadcast(request):
	# Get employees
	employees = Employee.objects.all()

	for employee in employees:

		# Send emails to each employees
		send_mail(
    	"ACS Coffee | Current debth",
    	"Dear " + employee.name + ",\n\nplease pay your outstanding coffee bill.\n\nDebth: " + str(employee.debth) + "€\nLast updated:" + str(employee.updated_at) + "\n\nThanks a lot and have a great day!",
    	"lukas.lenz@eonerc.rwth-aachen.de",
    	[employee.email],
    	fail_silently=False,
    	)

	context = {'employees':employees, 'output':"Successfully broadcasted to employees."}

	return render(request, 'main/index.html', context)