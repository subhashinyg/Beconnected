from distutils.log import error
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
import json

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
        
        return Response({"Products":product}) 
        #except:
        #    return Response({"Error":"Something Wrong"})
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
        try:
            catId=SubCategory.objects.filter(categories=request.data['categoryId'])

            serializer = SubCategorycreateSerializer(catId, many=True)
       
            return Response({"subcategories":serializer.data})
        except Exception as e:
            return Response({"subcategories":None})

        
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
        try:
            catId=Locations.objects.filter(subcategories=request.data['SubCategoryId'],category=request.data['CategoryId'])
            print(catId)

            serializer = LocationsSerializer(catId, many=True)
       
            return Response({"subcategoryLocations":serializer.data})
        except Exception as e:
            return Response({"subcategoryLocations":None})
        # subcategoryId = request.data['subcategoryId']
        # location = Locations.objects.all()
        # serializer = LocationsSerializer(location, many=True)
        # #print(serializer.data)
        # locationsList = serializer.data
        # return Response({"subcategories":locationsList})
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
        #try:
        serializer= BusinessServiceAddSerializer(data=request.data)
        print(serializer,'////////////////////////////////')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Business":serializer.data})
        #except Exception as e:
            #return Response({"Business":None})
    def get(self, request):
        location= request.data['locationid']
        category= request.data['categoryid']
        sub_category= request.data['subcategoryid']

        qs= BusinessServices.objects.filter(category=category, subcategory=sub_category, location=location)
        # qs= BusinessServices.objects.filter(location__subcategory__category__id=category, location__subcategory__id=sub_category, location=location)
        serial = BusinessServiceAddSerializer(qs, many= True)
        return Response({"Response":serial.data})
        

        #     return Response({
        #         'hasError': False,
        #         'message': 'Success',
        #         'response': serializer
        #     }, status=status.HTTP_200_OK)
        # except Exception as e:
        #     return Response({
        #         'hasError': True,
        #         'message': f'Failed: {str(e)}',
        #         'response': None
        #     }, status=status.HTTP_200_OK)

class ShopDescriptionView(APIView):
    def get(self,request, *args, **kwargs):
        try:
            data=BusinessServices.objects.get(id=request.data['id'])
            print(data,'/////////////////')
           
            # serializ= BusinessServicesList(data= data)
            # serializ.is_valid()
            return Response({"details":data})
        except:
            return Response({"error":"not found"})
class ShopDescriptionView(APIView):
    def get(self, request):
        try:
            shop_descriptions = BusinessServicesList(data=BusinessServices.objects.filter(id=request.data['id'])
            )
            return Response({
                'hasError': False,
                'message': 'Success',
                'response': shop_descriptions
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'hasError': True,
                'message': f'Failed: {str(e)}',
                'response': None
            }, status=status.HTTP_200_OK)
