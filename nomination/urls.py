#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  - URL configuration file of nomination module.   #
#                                                   #
#####################################################


from django.conf.urls import url

from . import views

app_name = 'nomination'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
]