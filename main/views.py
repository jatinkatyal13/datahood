from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import DataSet
from .forms import LoginForm

# Create your views here.

@login_required
def index(request):
	return render(request, 'main/index.html', {})

def login(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	invalid = False
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['user']
			password = form.cleaned_data['password']

			user = authenticate(username = username, password = password)

			if user is not None:
				login(request, user)
				try:
					return HttpResponseRedirect(request.GET['next'])
				except:
					return HttpResponseRedirect('/')
			else:
				invalid = True

	else:
		form = LoginForm(request.POST)

	params = {
		'form' : form,
		'invalid' : invalid
	}

	return render(request, 'main/login.html', params)