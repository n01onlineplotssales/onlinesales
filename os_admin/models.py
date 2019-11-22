from django.db import models

class AdminLogin(models.Model):
    a_contact_no = models.BigIntegerField(primary_key=True)
    a_password = models.CharField(max_length=20)
    a_otp = models.IntegerField()

class Agent(models.Model):
    ag_no = models.IntegerField()
    ag_name = models.CharField(max_length=50)
    ag_photo = models.ImageField(upload_to='agent/')
    ag_address = models.TextField()
    ag_contact_no = models.BigIntegerField()
    ag_username = models.CharField(primary_key=True, max_length=30)
    ag_password = models.CharField(max_length=20)
    ag_otp = models.IntegerField()

