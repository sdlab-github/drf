# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from weather.models import Light,Forecastingtime,City
from weather.serializers import LightSerializer
from rest_framework import generics

class LightList(generics.ListAPIView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer
    
    def get_queryset(self):
        queryset = Light.objects.all()
        Region = self.request.query_params.get('Region', None)
        Date = self.request.query_params.get('Date', None)
        if Region is not None and Date is not None:
            c=City.objects.get(CityName=Region)
            ft=Forecastingtime.objects.get(Forecastingtime=Date)
            queryset = queryset.filter(C_ID=c).filter(FT_ID=ft)
        elif Region is not None :
            c=City.objects.get(CityName=Region)
            queryset = queryset.filter(C_ID=c)
        elif Date is not None :
            ft=Forecastingtime.objects.get(Forecastingtime=Date)
            queryset = queryset.filter(FT_ID=ft)
        return queryset

