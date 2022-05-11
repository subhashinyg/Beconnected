from django.db import models
from user_app.models import *

# Create your models here.


class Shop_profile(models.Model):
    shop_image_1 = models.ImageField(upload_to='images')
    shop_image_2 = models.ImageField(upload_to='images')    
    shop_image_3 = models.ImageField(upload_to='images')   
    shop_image_4 = models.ImageField(upload_to='images')
    shop_name = models.CharField(max_length=100)
    shop_location = models.CharField(max_length=500)
    shop_phone = models.CharField(max_length=15)
    shop_phone2 = models.CharField(max_length=15)
    shop_details = models.CharField(max_length=100)
    shop_description = models.CharField(max_length=500)
    user =  models.ForeignKey(Account,on_delete=models.CASCADE)

    class Meta:
        db_table = "Shop_profile"

    def __str__(self):
        return self.shop_name