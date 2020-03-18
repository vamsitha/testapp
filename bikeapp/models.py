from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	bike_name = models.CharField(max_length=100, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	phone_num = models.IntegerField(unique=True, null=True, blank=True)
	time = models.DateTimeField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	
class bikeotp(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	otp = models.IntegerField()
