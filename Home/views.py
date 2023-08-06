from django.shortcuts import redirect, render
from django.http import HttpResponse 
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
    return render(request,'pages/register.html')
def Location(request):
    return render(request,'pages/Locations.html')
    