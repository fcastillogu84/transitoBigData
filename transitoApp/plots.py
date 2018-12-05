
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource
from bokeh.transform import dodge

import pandas as pd
from math import pi
from bokeh.palettes import Category20c
from bokeh.transform import cumsum


def image1(request):	
   

	title_plot_1 = "Genero Vs Vehiculos"
	x_axis_1 = "Genero"
	y_axis_1 = "Vehiculos"
	plot_1_width = 1000
	plot_1_height = 300

	plot_1 = figure(title= title_plot_1,  x_axis_label= x_axis_1, y_axis_label= y_axis_1, plot_width= plot_1_width,  plot_height= plot_1_height)

	plot_1.circle(x, y)
	plot_1.line(x, y, legend='' , line_width =2)

	script_1, div_1 = components(plot_1)

	graphic1 = {'script_image1':script_1, 'div_image1':div_1}
	return graphic1



def plot_proyeccion():

	x = {
   	 'Equipo1': 157,
    	 'Equipo2': 93,	
	}

	data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
	data['angle'] = data['value']/data['value'].sum() * 2*pi
		

	data['color'] = ['#6baed6', '#9ecae1']

	plot = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

	plot.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

	plot.axis.axis_label=None	
	plot.axis.visible=False
	plot.grid.grid_line_color = None

	script, div = components(plot)
	graphic2 = {"script_proyeccion" : script, "div_proyeccion" : div}

	return graphic2
