from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('loginn',views.loginn,name='loginn'),
        path('logoutt',views.logoutt,name='logoutt'),
    path('registers',views.registers,name='registers'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
]
