from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    active = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"
    
    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategories')
    subcategory_name = models.CharField(max_length=100,unique=True)
    active = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sub_category"

    def __str__(self):
        return self.subcategory_name


class Locations(models.Model):
    subcategories = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='subcategorylocation')
    location_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "locations"

    def __str__(self):
        return self.location_name

class BusinessServices(models.Model):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    name = models.CharField(max_length=62)
    description = models.CharField(max_length=255)
    address = models.TextField()
    phone_no = models.CharField(max_length=16)
    landline_no = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'business_services'
        verbose_name = 'Business Service'
        verbose_name_plural = 'Business Services'

    def __str__(self):
        return self.name