from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
	debt = forms.CharField( max_length=255)
	coffees = forms.IntegerField()
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username','password'] 