from django.db import models

class Client(models.Model):
    c_name = models.CharField(max_length=30)
    c_contact_no = models.IntegerField()
    c_photo = models.ImageField(upload_to='client/')
    c_address = models.TextField()
    c_username = models.CharField(primary_key=True, max_length=50)
    c_password = models.CharField(max_length=30)
    c_otp = models.IntegerField()

class Complaint(models.Model):
    comp_no = models.AutoField(primary_key=True)
    comp_client_un = models.ForeignKey(Client, on_delete=models.CASCADE)
    comp_complaint = models.TextField()