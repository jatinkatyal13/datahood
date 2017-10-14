from django import forms
from .models import DataSet

class LoginForm(forms.Form):
	user = forms.CharField(max_length=100)
	password = forms.CharField(widget = forms.PasswordInput)

class AddDataSetForm(forms.ModelForm):
	class Meta:
		model = DataSet
		fields = ['user', 'title', 'description', 'file']
