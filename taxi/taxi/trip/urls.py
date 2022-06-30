from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	
	path('',views.tripdetails,name="trip"),
	path('validate',views.validate, name ='validate'),
	path('success',views.success, name ='success'),
	path('complete',views.complete, name ='complete'),
	path('history',views.history, name ='history'),



]