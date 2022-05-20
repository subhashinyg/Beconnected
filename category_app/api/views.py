from operator import sub
from django.shortcuts import render
from category_app.models import *
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from category_app.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count
from django.core import serializers
from rest_framework import viewsets

# Create your views here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  pass

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        product= serializer.data
        d={}
        li=[]
        try:
            for i in range(len(product)):
                li.append({"id":product[i]['id'],"category_name":product[i]['category_name']})
            d['categories']=li
            return Response(d) 
        except:
            return Response({"Error":"Something Wrong"})
    def post(self, request):
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors)



class Categoryupdate(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'Error':'category not found'}, status=status.HTTP_404_NOT_FOUND)    

        serializer = CategorySerializer(category)
        return Response(serializer.data)



    def put(self, request, pk):

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            


class SubCategoryView(APIView):
    def get(self, request):
        subcategory = SubCategory.objects.all()
        serializer = SubCategorycreateSerializer(subcategory, many=True)
        subproduct = serializer.data
        d={}
        li=[]
        for i in range(len(subproduct)):
            li.append({"categories":subproduct[i]["categories"],"subcategory_name":subproduct[i]["subcategory_name"]})
        d["subcategory"]=li
        return Response(d) 
        
    def post(self, request):
        
        serializer = SubCategorycreateSerializer(data=request.data) 
        if serializer.is_valid():
            print(serializer.validated_data,"////////////////////////////////////")
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors)



class LocationView(APIView):
    def get(self, request):
        location = Locations.objects.all()
        serializer = LocationsSerializer(location, many=True)
        #print(serializer.data)
        locationsList = serializer.data
        li=[]
        d={}
        for i in range(len(locationsList)):
            li.append({"subcategories":locationsList[i]["subcategories"],"location_name":locationsList[i]["location_name"]})
        d["location"]=li
        return Response(d)
    def post(self, request):
        serializer = LocationsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors)

@api_view(['GET',])
def Subcategory(request,pk):
    sub_categories = Category.objects.get(pk=pk)
    serializer = ListingCategorySerializer(sub_categories)
    return Response(serializer.data)

class BusinessServicesView(APIView):
    def post(self, request):
        try:
            location_id = request.data['locationId']
            business_services = BusinessServicesList(
                BusinessServices.objects.filter(location=location_id), many=True
            ).data
            return Response({
                'hasError': False,
                'message': 'Success',
                'response': business_services
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'hasError': True,
                'message': f'Failed: {str(e)}',
                'response': None
            }, status=status.HTTP_200_OK)