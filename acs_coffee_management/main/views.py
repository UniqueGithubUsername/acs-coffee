import datetime
import csv
import openpyxl
import pandas as pd
from decimal import Decimal

from django.shortcuts import redirect, render
from django.core.mail import send_mail, send_mass_mail

from .models import Employee

def index(request):
	employees = Employee.objects.all()
	context = {'employees':employees}
	return render(request, 'main/index.html', context)

def importxlsx(request):
	df = pd.read_excel('2024-09-12_employees_input.xlsx')
	
	for index, row in df.iterrows():
		print(row['name'])
		print(row['qr'])
		print(row['email'])
		print(row['debth'])
		obj, created = Employee.objects.get_or_create(name=row['name'], qr=row['qr'], email=row['email'], debth=row['debth'], coffees=row['coffees'])

	employees = Employee.objects.all()
	context = {'employees':employees}
	return render(request, 'main/index.html', context)

def export(request):
	employees = Employee.objects.all()
	# Save as .csv
	df = pd.DataFrame(o.__dict__ for o in employees)
	# Remove timezone from columns
	df['updated_at'] = df['updated_at'].dt.tz_localize(None)
	df.to_excel(str(datetime.date.today()) + "_employees.xlsx")
	context = {'employees':employees, 'output':"Successfully exported " + str(datetime.date.today()) + "_employees.xlsx"}
	return render(request, 'main/index.html', context)

def broadcast(request):
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

def add(request, id):
	employee = Employee.objects.get(id=id)
	print(employee.name)
	print(employee.coffees)
	employee.coffees = employee.coffees + 1
	employee.save()


	employees = Employee.objects.all()
	context = {'employees':employees}
	return render(request, 'main/index.html', context)