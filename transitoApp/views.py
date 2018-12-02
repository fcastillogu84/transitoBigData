from django.shortcuts import render

#import para bokeh

from bokeh.plotting import figure 
from bokeh.embed import components



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

	x = [i for i in rage(2016,2020)]
	#x = [2016,2017,2018,2019]
	y = [6, 10, 17, 21]


	title_plot_1 = "Miembros del Semillero"
	x_axis_1 = "Años"
	y_axis_1 = "Miembros"
	plot_1_width = 500
	plot_1_height = 350

	plot_1 = figure(title= title_plot_1,  x_axis_label= x_axis_1, y_axis_label= y_axis_1, plot_width= plot_1_width,  plot_height= plot_1_height)

	plot_1.circle(x,y)
	plot_1.line(x,y,legend='' , line_width =2)

	script_1, div_1 = components(plot_1)

	return render(request, 'transitoApp/index.html', {'script_plot_1':script_1, 'div_plot_1':div_1})