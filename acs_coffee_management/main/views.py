import datetime
import csv
import openpyxl
import pandas as pd

from decimal import Decimal

from django.shortcuts import redirect, render
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.decorators import login_required

from .models import Employee, Coffee
from .forms import EmployeeForm

baseurl = "http://137.226.248.61:31387/user/"
addurl = "http://137.226.248.61:31387/add/"
coffee_price = 30

def index(request):
	employees = Employee.objects.all()
	current_time = datetime.datetime.now()

	coffees_today =Coffee.objects.filter(date__year=current_time.year,date__month=current_time.month,date__day=current_time.day).count() 
	coffees_week = Coffee.objects.filter(date__range=[current_time-datetime.timedelta(days=7), current_time]).count()
	coffees_month = Coffee.objects.filter(date__range=[current_time-datetime.timedelta(days=30), current_time]).count()
	coffees_total = Coffee.objects.all().count()

	context = {'employees':employees,'today':coffees_today,'week':coffees_week,'month':coffees_month,'total':coffees_total}
	return render(request, 'main/index.html', context)

def faq(request):
	context = {}
	return render(request, 'main/faq.html', context)

def importxlsx(request):
	df = pd.read_excel('employees_input.xlsx')
	
	for index, row in df.iterrows():
		print(row['name'])
		print(row['qr'])
		print(row['email'])
		print(row['debt'])
		print(row['coffees'])
		obj, created = Employee.objects.update_or_create(name=row['name'], email=row['email'], defaults={'qr':row['qr'], 'debth':row['debt'], 'coffees':row['coffees']})

	employees = Employee.objects.all()
	output = "Successfully imported employees_input.xlsx"
	context = {'employees':employees, 'output':output}
	return render(request, 'main/index.html', context)

def export(request):
	employees = Employee.objects.all()
	# Save as .csv
	#df = pd.DataFrame(o.__dict__ for o in employees)
	# Remove timezone from columns
	#df['updated_at'] = df['updated_at'].dt.tz_localize(None)
	#df.to_excel(str(datetime.date.today()) + "_employees.xlsx")

	employees_export = Employee.objects.values_list('name','qr','email','debth','coffees')
	print(employees_export)
	df = pd.DataFrame(data=employees_export, columns=['name','qr','email','debt','coffees'])
	df.to_excel(str(datetime.date.today()) + "_employees.xlsx")


	output = "Successfully exported " + str(datetime.date.today()) + "_employees.xlsx"
	context = {'employees':employees, 'output':output}
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
            output = "Successfully added new employee."
            context = {'employees':employees, 'output':output}
            return render(request, 'main/index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm()

    return render(request, "registration/login.html", {"form": form})


def mailtoemployee(request, id):
	employee = Employee.objects.get(id=id)
	# Send email to one employee
	text = "Dear " + employee.name + ",\n\n\nthe link to your coffee profile:\n" + baseurl + employee.qr + "\n\nOr to add a cup directly use this link:\n" + addurl + employee.qr + "\n\nYour current coffee bill:\n" + str(employee.debth) + "€\n\nYour current cups (not calculated in the current bill):\n" + str(employee.coffees) + "\n\n\nCheers!"
	send_mail(
		"ACS Coffee | Current debth",
		text,
		"lukas.lenz@eonerc.rwth-aachen.de",
		[employee.email],
		fail_silently=False,)

	employees = Employee.objects.all()
	output = "Successfully emailed to " + employee.name + "."
	context = {'employees':employees, 'output':output}
	return render(request, 'main/index.html', context)

def getlink(request, id):
	employee = Employee.objects.get(id=id)
	# Send emails to each employees
	global addurl, baseurl

	text = "Dear " + employee.name + ",\n\n\nthe link to your coffee profile:\n" + baseurl + employee.qr + "\n\nOr to add a cup directly use this link:\n" + addurl + employee.qr + "\n\nYour current coffee bill:\n" + str(employee.debth) + "€\n\nYour current cups (not calculated in the current bill):\n" + str(employee.coffees) + "\n\n\nCheers!"

	send_mail(
		"ACS Coffee | Current debth",
		text,
		"lukas.lenz@eonerc.rwth-aachen.de",
		[employee.email],
		fail_silently=False,)

	employees = Employee.objects.all()
	current_time = datetime.datetime.now()

	coffees_today =Coffee.objects.filter(date__year=current_time.year,date__month=current_time.month,date__day=current_time.day).count() 
	coffees_week = Coffee.objects.filter(date__range=[current_time-datetime.timedelta(days=7), current_time]).count()
	coffees_month = Coffee.objects.filter(date__range=[current_time-datetime.timedelta(days=30), current_time]).count()
	coffees_total = Coffee.objects.all().count()
	output = "Successfully requested link for " + employee.name + "."
	context = {'employees':employees,'today':coffees_today,'week':coffees_week,'month':coffees_month,'total':coffees_total,'output':output}
	return render(request, 'main/index.html', context)

def calcdebth(request):
	employees = Employee.objects.all()
	global coffee_price

	for employee in employees:
		employee.debth = (employee.coffees * coffee_price) / 100 + float(employee.debth)
		employee.debth = round(employee.debth, 2)
		employee.coffees = 0
		employee.save()

	output = "Successfully added coffees to debt."
	context = {'employees':employees, 'output':output}
	return render(request, 'main/index.html', context)

def broadcast(request):
	employees = Employee.objects.all()
	for employee in employees:
		# Send emails to each employees
		text = "Dear " + employee.name + ",\n\n\nthe link to your coffee profile:\n" + baseurl + employee.qr + "\n\nOr to add a cup directly use this link:\n" + addurl + employee.qr + "\n\nYour current coffee bill:\n" + str(employee.debth) + "€\n\nYour current cups (not calculated in the current bill):\n" + str(employee.coffees) + "\n\n\nCheers!"
		send_mail(
    	"ACS Coffee | Current debth",
    	text,
    	"lukas.lenz@eonerc.rwth-aachen.de",
    	[employee.email],
    	fail_silently=False,
    	)
	context = {'employees':employees, 'output':"Successfully broadcasted to employees."}
	return render(request, 'main/index.html', context)

def user(request, slug):
	employee = Employee.objects.get(qr=slug)
	coffees = employee.coffee_set.all()
	context = {'employee':employee, 'coffees':coffees}
	return render(request, 'main/user.html', context)

def add(request, slug):
	employee = Employee.objects.get(qr=slug)
	employee.coffees = employee.coffees + 1
	employee.save()
	coffee = Coffee(user=employee)
	coffee.save()
	date = coffee.date
	#get all coffees
	coffees = employee.coffee_set.all()
	output = "Added 1 cup just now"
	context = {'employee':employee, 'coffees':coffees, 'output':output}
	return render(request, 'main/user.html', context)