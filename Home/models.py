from django.db import models

# Create your models here. Database Storage 

class Food(models.Model):
    x = [
        ('Breakfast','Breakfast'),('Launch','Launch'),('Dinner','Dinner')
    ]
    name = models.CharField(max_length=50,verbose_name='Dish Name')
    content = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=3,decimal_places=2)
    image = models.ImageField(verbose_name='Picture',upload_to='images/FoodPics')
    category = models.CharField(max_length=50,blank=True,choices=x)

class Messages(models.Model):
    Contact_Name = models.CharField(max_length=50)
    Contact_Email = models.TextField()
    Message = models.TextField()

class News(models.Model):
    Head = models.CharField(max_length=50,verbose_name='Main Title')
    Description = models.TextField()
    News_image = models.ImageField(upload_to='images/News_Pics',verbose_name='Photo')

class Blog(models.Model):
    H_name = models.CharField(max_length=50,verbose_name='Main Title')
    Details = models.TextField()

class user(models.Model):
    FullName = models.CharField(max_length=50,verbose_name='Name')
    Email = models.TextField()
    Password = models.CharField(max_length=16)
    USER_Id = models.ImageField(upload_to='images/User_Ids',verbose_name='Id Photo')
    Profile = models.ImageField(upload_to='images/User_Profiles',verbose_name='Profile Photo',default='images/avatar.png')