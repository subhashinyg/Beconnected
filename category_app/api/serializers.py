from rest_framework import serializers
from stripe import Source
from category_app.models import *


class CategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Category
        fields = ['id','category_name']

class SubCategorycreateSerializer(serializers.ModelSerializer):
    categories = CategorySerializer

    class Meta:
        model = SubCategory
        fields = ['id','subcategory_name','categories']


class SubCategorySerializer(serializers.ModelSerializer):
    categories = serializers.CharField(source='categories.category_name')

    class Meta:
        model = SubCategory
        fields = ['id','subcategory_name','categories'] 


class LocationsSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer

    class Meta:
        model = Locations
        fields = ['id','location_name','subcategories']               



class ListingCategorySerializer(serializers.ModelSerializer):

    
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['subcategories']

class BusinessServicesList(serializers.ModelSerializer):
    serviceId = serializers.IntegerField(source='id')
    category = serializers.CharField(source='category.category_name')
    subcategory = serializers.CharField(source='subcategory.subcategory_name')
    phoneNo = serializers.CharField(source='phone_no')
    landlineNo = serializers.CharField(source='landline_no')
    class Meta:
        model = BusinessServices
        fields = ('serviceId', 'name', 'description', 'address', 'phoneNo', 'landlineNo', 'category', 'subcategory')
