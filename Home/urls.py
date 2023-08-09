from django.http import HttpResponse
from . import views
from django.urls import path
urlpatterns = [
        path('',views.Home,name='home'), #path will be added after the / that comes after tha / that comes after the DN :(
        path('about/',views.About,name='about'),
        path('blog/',views.Blog,name='blog'),
        path('testi/',views.Testi,name='testi'),
        path('login/',views.login,name='login'),
        path('register/',views.Register,name='register'),
        path('location/',views.places,name='location'),
        path('cart',views.Cart,name='cart'),
        path('menu',views.Menu,name='menu'),
]


