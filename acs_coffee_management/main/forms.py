from django import forms
from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
        	'name': forms.TextInput(attrs={'placeholder': 'Last name, First name'}),
        	'qr': forms.TextInput(attrs={'placeholder': 'https://localhost:8000/user/<your-link>'}),
        	'email': forms.TextInput(attrs={'placeholder': 'Insert work email'}),
        	'debth': forms.TextInput(attrs={'placeholder': 'e.g. 13.50'})
        }
        labels = {
        	'name' : "Name:",
        	'qr' : "Access link:",
        	'email' : "Email:",
        	'debth' : "Debt of account:",
        	'coffees' : "New coffees:",
        }