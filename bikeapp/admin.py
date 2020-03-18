from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from . models import User
from . models import bikeotp
# Register your models here.

admin.site.register(User)
admin.site.register(bikeotp)