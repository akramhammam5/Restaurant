from django.contrib import admin
from .models import *
# Register your models here. Add data to DB.


admin.site.register(User)

admin.site.register(New)

admin.site.register(Blog)

admin.site.register(Message)

admin.site.register(reserve)
