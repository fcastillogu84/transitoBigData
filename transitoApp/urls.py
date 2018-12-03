from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^forgotPassword/$', views.forgotPassword, name='forgotPassword'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^tables/$', views.tables, name='tables'),
    url(r'^index/$', views.viewStaff, name='viewStaff'),
   
]

