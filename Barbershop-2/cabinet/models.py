from django.db import models

class Application(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       status = models.CharField(max_length=100, choices=[('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed')])

       def __str__(self):
           return self.title
