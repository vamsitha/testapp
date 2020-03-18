from django.urls import path

from . import views

urlpatterns = [
    path('bookride/', views.register, name='register'),
    path('otp/', views.checkotp, name='checking'),
    path('getperson/', views.person_get, name='getperson'),
   ]