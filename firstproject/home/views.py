from audioop import reverse
from multiprocessing import context
from ssl import AlertDescription
from turtle import home
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Booking,Departments,Doctors
from .forms import BookingForm, SignupForm
from django.contrib import messages
# Create your views here.
def index(request):
    number={'num1':[1,2,3,4,5,6,7,8,9]
        
    }
    return render(request,'index.html',number)
def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form= BookingForm(request.POST)
        if form.is_valid():
            dname= Doctors.doc_name
            name1 = request.POST.get('p_name')
            form.save()
            dict_form = {
                'p_name':name1,'doc_name':dname
                        }
            return render(request,'confirmation.html',dict_form)
    form= BookingForm(request.POST)
    username = User.username
    p = {
        'form':form
        }      
    return render(request,'booking.html',p)

def registers(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'success.html',{'alert_flag': False})
    form = SignupForm(request.POST)
    context ={'form': form}
    return render(request,'signup.html',context)

def loginn(request):         
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            #return render(request,'base2.html',{'alert_flag': True,'username':username})
            return redirect('booking')
        else:
            messages.info(request, "Ooops!Incorrect Username Or password!!")
    return render(request,'loginn.html')
       
def logoutt(request):
    logout(request)
    return redirect(request,'base1.html')


def doctors(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)