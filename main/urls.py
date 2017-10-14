from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/?$', views.login_view, name='login'),
	url(r'^logout/?$', views.logout_view, name='logout'),
	url(r'^get_datasets/(?P<page>[0-9]+)/?$', views.get_recent_data_sets, name='get_datasets'),
]