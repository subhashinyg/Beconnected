from distutils.log import error
from operator import sub
from urllib import response
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
        try:
            location_Id= request.data['locationid']
            category= request.data['categoryid']
            sub_category= request.data['subcategoryid']
            print(location_Id,category,sub_category)
            qs= BusinessServices.objects.filter(category=category, subcategory=sub_category, location=location_Id)
            # qs= BusinessServices.objects.filter(location__subcategory__category__id=category, location__subcategory__id=sub_category, location=location)
            serial = BusinessServiceAddSerializer(qs, many= True)
            return Response({"Response":serial.data})
        except Exception as e:
            return Response(e)

        

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

# class ShopDescriptionView(APIView):
#     def get(self,request, *args, **kwargs):
#         try:
#             cs = BusinessServices.objects.all()
#             serializer = BusinessServiceAddSerializer(cs, many=True)
#             return JsonResponse({"cs": serializer.data}, safe=False, status=status.HTTP_200_OK)
           
# #             # serializ= BusinessServicesList(data= data)
# #             # serializ.is_valid()
# #             return Response({"details":data})
#         except Exception as e:
#             return Response({"error":e})

class ShopDescriptionView(APIView):
    def get(self, request):
        business = request.data['id']
        des = BusinessServices.objects.filter(id=business)
        print(des,'[[[[[[[[[[[[[[[[[[[[[[')
        shop_descriptions = BusinessServiceAddSerializer(des,many=True)
        print(shop_descriptions,'///')
        # data={
        #     #'serviceId':shop_descriptions.serviceId,
        #     #'name':shop_descriptions.name,
        #     'address':shop_descriptions.address,
        #     'phoneNo':shop_descriptions.phone_no
            
        # }
            #shop_descriptions = BusinessServicesList.objects.all()
        return Response(shop_descriptions.data)


class PrivacyView(APIView):
    def get(self, request):
        Privacy_policy = PrivacyPolicy.objects.all()
        print(Privacy_policy,'''''''''''''''''''''''''''''''''''''''''''')
        serial = PrivacyPolicySerializer(Privacy_policy, many = True)
        return Response({"policy":serial.data}) 


def policy(request):
    return render(request, 'policy.html')