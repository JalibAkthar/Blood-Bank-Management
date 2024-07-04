from django.db import models

# Create your models here.

class DonarDB(models.Model):
    Donar_Name = models.CharField(max_length=100,null=True,blank=True)
    Age = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Blood_Group = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Profile_Image = models.ImageField(upload_to="d_images",null=True,blank=True)

class RecipientDB(models.Model):
    Recipient_Name = models.CharField(max_length=100, null=True, blank=True)
    R_Age = models.IntegerField(null=True, blank=True)
    R_Mobile = models.IntegerField(null=True, blank=True)
    R_Blood_Group = models.CharField(max_length=100, null=True, blank=True)
    R_Quantity = models.CharField(max_length=100,null=True,blank=True)
    R_Date = models.CharField(max_length=100,null=True,blank=True)
    R_Email = models.CharField(max_length=100, null=True, blank=True)
    R_Place = models.CharField(max_length=100, null=True, blank=True)
    R_Address = models.CharField(max_length=100, null=True, blank=True)
    R_Profile_Image = models.ImageField(upload_to="r_images", null=True, blank=True)