from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.

##customize user
class Users(AbstractUser):
    # Add any additional fields you want to store for your users here
    # For example, you might want to store their age or address:
    #email = models.EmailField(unique=True)
    #token = models.OneToOneField(Token, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

class Flows(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    flow_title = models.CharField(max_length=30)
    flow_overview = models.CharField(max_length=100)
    flow_content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

