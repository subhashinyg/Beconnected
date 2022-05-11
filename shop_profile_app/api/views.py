from django.shortcuts import render
from shop_profile_app.models import *
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from shop_profile_app.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count
from django.core import serializers
from rest_framework import viewsets

# Create your views here.


class Shop_profileView(APIView):
    def get(self, request):
        shops = Shop_profile.objects.all()
        serializer = shopSerializer(shops, many=True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = shopSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'shops':serializer.data})   
        else:
            return Response(serializer.errors)



class shop_profile_edit(APIView):

    def get(self, request, pk):
        try:
            shop = Shop_profile.objects.get(pk=pk)
        except Shop_profile.DoesNotExist:
            return Response({'Error':'shop not found'}, status=status.HTTP_404_NOT_FOUND)    

        serializer = shopSerializer(shop)
        return Response(serializer.data)



    def put(self, request, pk):

        shop = Shop_profile.objects.get(pk=pk)
        serializer = shopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        shop = Shop_profile.objects.get(pk=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 