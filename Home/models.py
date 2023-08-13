from django.db import models



class Food(models.Model):
    x = [
        ('Breakfast','Breakfast'),('Launch','Launch'),('Dinner','Dinner')
    ]
    name = models.CharField(max_length=50,verbose_name='Dish Name')
    content = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=3,decimal_places=2)
    image = models.ImageField(verbose_name='Picture',upload_to='images/FoodPics')
    category = models.CharField(max_length=50,blank=True,choices=x)
    Amount = models.IntegerField(default=25,blank=True)

class Message(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Email = models.TextField(null=True)
    message = models.TextField(null=True)
    
class New(models.Model):
    Head = models.CharField(max_length=50,verbose_name='Main Title')
    Description = models.TextField()
    News_image = models.ImageField(upload_to='images/News_Pics',verbose_name='Photo')
    class Meta:
         db_table = 'News'
class Blog(models.Model):
    H_name = models.CharField(max_length=50,verbose_name='Main Title')
    Details = models.TextField()
    
class User(models.Model):
    username = models.CharField(max_length=50,verbose_name='Name',null=True,default='User')
    Email = models.TextField(null=True)
    password = models.CharField(null=True,max_length=16)
    photo = models.ImageField(upload_to='images/User_Ids',verbose_name='Id Photo',null=True)

    class Meta:
         db_table = 'Users'
class reserve(models.Model):
    name = models.CharField(max_length=50)
    date = models.TextField()
    Email = models.TextField()
    phone = models.TextField()