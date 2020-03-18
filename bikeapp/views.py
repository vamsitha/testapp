from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from rest_framework.decorators import api_view
import random
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from Bike import settings
from . models import User
from . models import bikeotp
from django.http import JsonResponse
import json

# Create your views here.


@api_view(['POST'])
def register(request):
	if request.method == 'POST':
		personname = request.POST['username']
		bikename = request.POST['bikename']
		phonenum = request.POST['phonenum']
		email = request.POST['email']
		time = request.POST['time']
		otp = random.randrange(111111,999999,6)
		top = '{}'.format(otp)		
		v_mail = send_mail(
        	"subject",
        	top,
        	settings.EMAIL_HOST_USER,
        	[email], 
        	fail_silently= True,
    		)
		data = User.objects.create(
			username = personname,
			bike_name=bikename,
			email=email,
			phone_num=phonenum,
			time=time,
			)
		data.is_active = False
		data.save()
		otp_data = bikeotp.objects.create(user=data, otp=top)
		otp_data.save()
		info = "user created"
		return JsonResponse({'success':True,'info':info})
	else:	
		info = "Failed to register,Use Postman"
		return JsonResponse({'success':False,'info':info})



@api_view(['POST'])
def checkotp(request):
	if request.method == 'POST':
		p_email = request.POST['email']
		p_otp = request.POST['num']
		user_instance = User.objects.get(email = p_email)
		data = bikeotp.objects.get(otp = p_otp)
		if user_instance.email == p_email:
			if data.otp == int(p_otp):
				user_instance.is_active = True
				user_instance.save()
				new = '{} {}'.format(data.user,data.otp)
				p_mail = send_mail(
					"subject",
					new,
					settings.EMAIL_HOST_USER,
					['vamsitha12@gmail.com'], 
					fail_silently= True,
				)
				info = "otp matched"
				return JsonResponse({'success':True,'info':info})
		else:
			info = "failed"
			return JsonResponse({'success':False,'info':info})
	else:
		info = "no, Use Postman"
		return JsonResponse({'success':True,'info':info})


@api_view(['GET'])
def person_get(request):
	if request.method == 'GET':
		data = User.objects.filter(is_active=True).values_list('id','username','is_active')
		info = list(data.values())
		return JsonResponse({'success':True,'info':info})

