from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from .models import Message,User,Blog,New,reserve
from django.contrib.auth.decorators import login_required
def Home(request):
    RestaurantName = {'Name':'los Pollos Hermanos'}
    return render(request,'pages/index.html',RestaurantName) #The last contxt is used as an example for retreiving data from DB
def About(request):
    return render(request,'pages/about.html')
def blog(request):
    data = Blog.objects.all()
    return render(request,'pages/blog.html',{'Blogs':data})
def Testi(request):
    return render(request,'pages/testimonial.html')
def loginn(request):
     if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pass')
        username_check = User.objects.filter(username=username).exists()
        password_check = User.objects.filter(password=password).exists()
        userr = authenticate(username=username_check, password=password)
        if username is not None and username_check and password_check:
            #login(request,userr)
            return render(request,'pages/Loginsession.html')
        else:  
            return redirect('error')    
     return render(request,'pages/login.html')
def Register(request):
    username = request.POST.get('full-name')
    Email = request.POST.get('email')
    password = request.POST.get('password')
    confirm = request.POST.get('conpassword')
    photo = request.POST.get('upload')
    if username is not None:
        if username_exists(username):
            return HttpResponse('This Username already exists!')
        else: 
            data = User(username=username, Email=Email, password=password, photo=photo)
            data.save()
            del request.session
            return render(request,'pages/index.html')
       
    return render(request,'pages/register.html')
def places(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            message = Message(Name=name, Email=email,message=message)
            message.save()
            return redirect('home')
        else:
            return render(request, 'pages/contact.html', {'error': 'Please fill out all of the fields.'})
    else:
        return render(request, 'pages/contact.html')
def Cart(request):
    return render(request,'pages/cart.html')
def Menu(request):
    return render(request,'pages/food_menu.html')
def Error(request):
    return render(request,'pages/Error.html')
def username_exists(username):
    return User.objects.filter(username=username).exists()
def passw_exists(password):
    return User.objects.filter(password=password).exists()

@login_required
def Session(request):
    return render(request,'pages/Loginsession.html')

def News(request):
    data = New.objects.all()
    return render(request,'pages/News.html',{'News':data})

def edit(request):
    return render(request,'pages/edit.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def submit(request):
    return render(request,'pages/submit.html')
def Reserve(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        if name and Email and phone:
                data = reserve(name=name, Email=Email,phone=phone,date=date)
                data.save()    
    
    return render(request,'pages/Reservations.html')