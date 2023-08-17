from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class UserProfile( models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	

	
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	followers=models.IntegerField(default=0)
	time= models.TimeField(auto_now=True)
	date=models.DateField(auto_now=True)
class Repository(models.Model):
	repo=models.CharField(max_length=100)
	star=models.IntegerField(default=0)
	profile= models.ForeignKey(Profile,on_delete=models.CASCADE)
			
	
	

	
	
