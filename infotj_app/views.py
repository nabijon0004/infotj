from django.shortcuts import render

from django.db.models import Q
from rest_framework import generics
from .models import Establishment
from .serializers import EstablishmentSerializer, EstablishmentListSerializer

class EstablishmentListAPIView(generics.ListAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentListSerializer

class EstablishmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

class EstablishmentCategoryListAPIView(generics.ListAPIView):
    serializer_class = EstablishmentListSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Establishment.objects.filter(type_of_establishment=category)

class EstablishmentCityListAPIView(generics.ListAPIView):
    serializer_class = EstablishmentListSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        return Establishment.objects.filter(city=city)
class EstablishmentAddressSearchAPIView(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        address = self.kwargs['address'].replace('-', ' ')
        return Establishment.objects.filter(address_street__icontains=address)

class EstablishmentNameSearchAPIView(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        name = self.kwargs['name'].replace('-', ' ')
        return Establishment.objects.filter(name__icontains=name)