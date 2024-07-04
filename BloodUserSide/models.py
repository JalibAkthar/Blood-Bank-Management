from django.db import models

# Create your models here.

class ContactDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)

class LoginDB(models.Model):
    L_Name = models.CharField(max_length=100,null=True,blank=True)
    L_Email = models.EmailField(max_length=100,null=True,blank=True)
    L_Password = models.CharField(max_length=100,null=True,blank=True)
    L_Mobile = models.IntegerField(null=True,blank=True)