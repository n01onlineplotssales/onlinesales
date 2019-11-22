from django.db import models
from os_admin.models import Agent
from os_client.models import Client

class Property(models.Model):
    p_no = models.AutoField(primary_key=True)
    p_agent_un = models.ForeignKey(Agent,on_delete= models.CASCADE)
    p_name = models.CharField(max_length=50)
    p_location = models.CharField(max_length=500)
    p_photo = models.ImageField(upload_to='property/')
    p_size = models.CharField(max_length=50)
    p_prize = models.CharField(max_length=50)
    p_facing = models.CharField(max_length=50)
    p_status = models.CharField(max_length=50)
    p_add_date = models.DateField(auto_now_add=True)
    p_sold_date = models.DateField(auto_now_add=True)
    p_comment = models.CharField(max_length=500, default='Good')

class SoldProperty(models.Model):
    s_property_no = models.ForeignKey(Property, on_delete=models.CASCADE)
    s_client_un = models.ForeignKey(Client, on_delete=models.CASCADE)
    s_date_of_sold = models.DateField(auto_now_add=True)

class BlockProperty(models.Model):
    b_block_property_no = models.AutoField(primary_key=True)
    b_property_no = models.ForeignKey(Property, on_delete=models.CASCADE)
    b_block_date = models.DateField(auto_now_add=True)
    b_client_un = models.ForeignKey(Client, on_delete=models.CASCADE)
    # b_amount = models.IntegerField()












