from rest_framework import serializers
from .models import Establishment, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']

class EstablishmentSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        fields = ['id', 'name', 'description', 'type_of_establishment', 'address_street', 'address_number', 'city', 'phone_number', 'second_phone_number', 'email', 'business_hours', 'photos']

class EstablishmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ['id', 'name', 'type_of_establishment', 'address_street', 'address_number', 'city']