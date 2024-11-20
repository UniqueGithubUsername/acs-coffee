from django import forms
from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
        	'name': forms.TextInput(attrs={'placeholder': 'Last name, First name'}),
        	'qr': forms.TextInput(attrs={'placeholder': 'http://137.226.248.61:31387/user/<your-link>'}),
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

class ChangeEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','qr']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Last name, First name'}),
            'qr': forms.TextInput(attrs={'placeholder': 'http://137.226.248.61:31387/user/<your-link>'}),
            'email': forms.TextInput(attrs={'placeholder': 'Insert work email'}),
        }
        labels = {
            'name' : "Name:",
            'qr' : "Access link:",
            'email' : "Email:",
        }

class ChooseEmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(label="",queryset=Employee.objects.all(),required=True)
    verify = forms.CharField(label="",max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Your email'}),required=True)