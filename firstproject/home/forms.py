from socket import fromshare
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking


class DateInput(forms.DateInput):
    input_type ='date'


class BookingForm(forms.ModelForm):
    
    class Meta:
        model =  Booking
        fields = ('__all__')

        widgets ={
            'booking_date' : DateInput(),
        }

        labels ={
            'p_name' : "Patient Name:",
            'p_phone' :  "Phone Number:",
            'p_email' : "E-mail:",
            'doc_name' : "Doctor:",
            'booking_date':"Date of booking:"
        }



class SignupForm(UserCreationForm): 
    class Meta:
        model =  User
        fields = ('username','email','password1','password2')


        

