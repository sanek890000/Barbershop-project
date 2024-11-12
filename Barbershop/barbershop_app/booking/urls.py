from django.urls import path
from . import views

urlpatterns = [
       path('', views.main_page, name='main_page'),
       path('thank-you/', views.thank_you_page, name='thank_you_page'),
       path('create-booking/', views.create_booking, name='create_booking'),
       path('fetch-services/', views.service_fetch, name='service_fetch'),
   ]