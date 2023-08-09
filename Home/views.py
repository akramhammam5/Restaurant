from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import *
# Create your views here.

def Home(request):
    RestaurantName = {'Name':'los Pollos Hermanos'}
    return render(request,'pages/index.html',RestaurantName) #The last contxt is used as an example for retreiving data from DB
def About(request):
    return render(request,'pages/about.html')
def Blog(request):
    return render(request,'pages/blog.html')
def Testi(request):
    return render(request,'pages/testimonial.html')
def login(request):
    return render(request,'pages/login.html')
def Register(request):
    Name = request.POST.get('full-name')
    Email = request.POST.get('email')
    password = request.POST.get('password')
    photo = request.POST.get('upload')
    Data = user(Name=Name,Email=Email,password=password,photo=photo)
    Data.save()
    #print(Data)
    return render(request,'pages/register.html')
def places(request):
    return render(request,'pages/contact.html')
def Cart(request):
    return render(request,'pages/cart.html')
def Menu(request):
    return render(request,'pages/food_menu.html')