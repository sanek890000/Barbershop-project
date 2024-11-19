from django.contrib.auth.models import AbstractUser
from django.db import models

class Service(models.Model):
       name = models.CharField(max_length=100)
       price = models.DecimalField(max_digits=6, decimal_places=2)

       def __str__(self):
           return self.name

class Master(models.Model):
       first_name = models.CharField(max_length=50)
       last_name = models.CharField(max_length=50)
       contact_info = models.TextField()
       photo = models.ImageField(upload_to='masters_photos/')
       services = models.ManyToManyField(Service)

       def __str__(self):
           return f'{self.first_name} {self.last_name}'

class Visit(models.Model):
       name = models.CharField(max_length=100)
       phone = models.CharField(max_length=15)
       master = models.ForeignKey(Master, on_delete=models.CASCADE)
       service = models.ForeignKey(Service, on_delete=models.CASCADE)

class CustomUser(AbstractUser):
       avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)