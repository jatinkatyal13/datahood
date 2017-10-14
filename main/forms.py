from django import forms
from . import models

class LoginForm(forms.Form):
	user = forms.CharField(max_length=100)
	password = forms.CharField(widget = forms.PasswordInput)