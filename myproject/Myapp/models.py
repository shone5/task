from django.db import models

# Create your models here.
class SalesData(models.Model):
    status = models.CharField(max_length=50,null=True,blank=True)
    year = models.CharField(max_length=50,null=True,blank=True)
    K = models.CharField(max_length=50,null=True,blank=True)
    M = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    orderno = models.IntegerField(null=True,blank=True)
    price = models.FloatField(null=True,blank=True)

