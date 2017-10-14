from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import DataSet
from .forms import LoginForm, AddDataSetForm
from django.core import serializers
import json

# Create your views here.

# APIs
@login_required
def get_recent_data_sets(request, page):

	MAX_ON_PAGE = 7

	page = int(page)

	data = DataSet.objects.all().order_by('-publishing_date')[page*MAX_ON_PAGE:page*MAX_ON_PAGE + MAX_ON_PAGE]

	res = list()

	for x in data:
		temp = dict()

		temp['name'] = User.objects.get(id = x.user.id).first_name
		temp['title'] = x.title
		temp['description'] = x.description
		temp['file'] = x.file.name

		res.append(temp)

	# for x in data:
	# 	x['fields']['name'] = User.objects.get(id = x['fields']['id']).first_name

	return HttpResponse(json.dumps(res))

# views
@login_required
def index(request):

	if request.method == "POST":
		form = AddDataSetForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			dataSet = DataSet(
				user = User.objects.get(id = request.user.id),
				title = form.cleaned_data['title'],
				description = form.cleaned_data['description'],
				file = request.FILES['file']
			)
			dataSet.save()
	else:
		form = AddDataSetForm()

	params = {
		'form' : form
	}

	return render(request, 'main/index.html', params)

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect('/login')
	else:
		raise Http404()

def login_view(request):

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