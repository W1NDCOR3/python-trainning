from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)
    
# class Task(models.Model):
#     id= models.BigAutoField(primary_key=True)
#     user =
    
    
