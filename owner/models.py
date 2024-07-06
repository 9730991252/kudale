from django.db import models

# Create your models here.
class Mukadam(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField()
    date = models.DateField(auto_now_add=True)



class Karkhana(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

class Taneg(models.Model):
    mukadam = models.ForeignKey(Mukadam,on_delete=models.PROTECT,default=True)
    karkhana = models.ForeignKey(Karkhana,on_delete=models.PROTECT,default=True)
    added_by = models.CharField(max_length=100,null=True)
    taneg = models.FloatField()
    date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)