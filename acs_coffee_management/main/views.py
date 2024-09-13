import datetime
import csv
import openpyxl
import pandas as pd
from decimal import Decimal

from django.shortcuts import redirect, render
from django.core.mail import send_mail, send_mass_mail

from .models import Employee
from .forms import EmployeeForm

def index(request):
	employees = Employee.objects.all()
	context = {'employees':employees}
	return render(request, 'main/index.html', context)

def importxlsx(request):
	df = pd.read_excel('employees_input.xlsx')
	
	for index, row in df.iterrows():
		print(row['name'])
		print(row['qr'])
		print(row['email'])
		print(row['debth'])
		print(row['coffees'])
		obj, created = Employee.objects.update_or_create(name=row['name'], email=row['email'], defaults={'qr':row['qr'], 'debth':row['debth'], 'coffees':row['coffees']})

	employees = Employee.objects.all()
	context = {'employees':employees, 'output':"Successfully imported employees_input.xlsx"}
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

def newemployee(request):
	# if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            employees = Employee.objects.all()
            context = {'employees':employees, 'output':"Successfully added new employee: "}
            return render(request, 'main/index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm()

    return render(request, "registration/login.html", {"form": form})


def mailtoemployee(request, id):
	employee = Employee.objects.get(id=id)
	# Send emails to each employees
	send_mail(
		"ACS Coffee | Current debth",
		"Dear " + employee.name + ",\n\nplease pay your outstanding coffee bill.\n\nDebth: " + str(employee.debth) + "€\nLast updated:" + str(employee.updated_at) + "\n\nThanks a lot and have a great day!",
		"lukas.lenz@eonerc.rwth-aachen.de",
		[employee.email],
		fail_silently=False,)

	employees = Employee.objects.all()
	context = {'employees':employees, 'output':"Successfully emailed to " + employee.name + "(" + employee.email + ")."}
	return render(request, 'main/index.html', context)

def calcdebth(request):
	employees = Employee.objects.all()
	coffee_price = 40
	for employee in employees:
		employee.debth = (employee.coffees * coffee_price) / 100 + float(employee.debth)
		employee.debth = round(employee.debth, 2)
		employee.coffees = 0
		employee.save()

	context = {'employees':employees, 'output':"Successfully added coffees to debth."}
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

def user(request, id):
	employee = Employee.objects.get(id=id)
	context = {'employee':employee}
	return render(request, 'main/user.html', context)

def add(request, slug):
	employee = Employee.objects.get(qr=slug)
	print(employee.name)
	print(employee.qr)
	print(employee.coffees)
	employee.coffees = employee.coffees + 1
	employee.save()

	context = {'employee':employee}
	return render(request, 'main/user.html', context)