from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from . import views

from django.urls import path
urlpatterns = [
        path('',views.Home,name='home'), #path will be added after the / that comes after tha / that comes after the DN :(
        path('about/',views.About,name='about'),
        path('blog/',views.blog,name='blog'),
        path('testi/',views.Testi,name='testi'),
        path('login/',views.loginn,name='login'),
        path('register/',views.Register,name='register'),
        path('location/',views.places,name='location'),
        path('cart/',views.Cart,name='cart'),
        path('menu/',views.Menu,name='menu'),
        path('error/',views.Error,name='error'),
        path('Home',views.Session,name='Home'),
        path('News/',views.News,name='News'),
        path('edit/',views.edit,name='edit'),
        path('logout/',views.user_logout,name='logout'),
        path('Message/',views.submit,name='submit'),
        path('reserve',views.Reserve,name='reserve'),

]       


