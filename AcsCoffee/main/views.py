from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import CoffeeUser
from .forms import RegisterForm

@login_required
def index(request):
	u = User.objects.get(id=request.user.id)
	c = u.coffeeuser.coffee_set.all()
	context = {'u':u, 'c':c}
	return render(request, 'main/index.html', context)

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			print("VALID")

			# Save user
			user = form.save()
			user.set_password(user.password)
			user.save()

			debt = form.cleaned_data['debt']
			coffees = form.cleaned_data['coffees']
			# Create coffee user
			cuser = CoffeeUser(user=user, debt=debt, coffees=coffees)
			cuser.save()

			print(cuser)
			context = {}
			return render(request, 'main/index.html', context)

	else:
		form = RegisterForm()
	
	context= {'form': form}

	return render(request, 'registration/login.html', context)

def addcup(request):
	u = User.objects.get(id=request.user.id)
	u.coffeeuser.coffees = u.coffeeuser.coffees + 1;
	u.coffeeuser.save()

	c = u.coffeeuser.coffee_set.all()
	context = {'u':u, 'c':c}
	return render(request, 'main/index.html', context)