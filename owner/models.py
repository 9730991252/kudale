from django.db import models

# Create your models here.
class Mukadam(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=100)
    pin = models.IntegerField(max_length=100)
    status = models.IntegerField(max_length=100)
    date = models.DateField(auto_now_add=True)

 

class Karkhana(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

class Vehicle(models.Model):
    owner_name = models.CharField(max_length=200)
    vehicle_number = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=100,null=True)
    pin = models.IntegerField(max_length=100,null=True)
    date = models.DateField(auto_now_add=True ,null=True)
    status = models.IntegerField(max_length=100)

class Taneg(models.Model):
    mukadam = models.ForeignKey(Mukadam,on_delete=models.PROTECT,default=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.PROTECT,null=True)
    karkhana = models.ForeignKey(Karkhana,on_delete=models.PROTECT,default=True)
    added_by = models.CharField(max_length=100,null=True)
    taneg = models.FloatField(max_length=100)
    date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)