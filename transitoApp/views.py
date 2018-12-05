import plots
from django.shortcuts import render


def charts(request):
	return render(request, 'transitoApp/charts.html')
def forgotPassword(request):
	return render(request, 'transitoApp/forgot-password.html')
def index(request):
	return render(request, 'transitoApp/index.html')
def login(request):
	return render(request, 'transitoApp/login.html')
def register(request):
	return render(request, 'transitoApp/register.html')
def tables(request):
	return render(request, 'transitoApp/tables.html')



def viewStaff(request):	
	parameters = {}
	parameters.update(plots.image1())
	parameters.update(plots.plot_proyeccion())
	   
	return render(request, 'transitoApp/index.html' , parameters)
