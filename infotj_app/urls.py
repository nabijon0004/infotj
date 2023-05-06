from django.urls import path
from .views import EstablishmentListAPIView, EstablishmentCategoryListAPIView, EstablishmentCityListAPIView, EstablishmentAddressSearchAPIView, EstablishmentNameSearchAPIView

urlpatterns = [
    path('establishments/', EstablishmentListAPIView.as_view(), name='establishment-list'),
    path('establishments/category/<slug:category>/', EstablishmentCategoryListAPIView.as_view(), name='establishment-category-list'),
    path('establishments/city/<slug:city>/', EstablishmentCityListAPIView.as_view(), name='establishment-city-list'),
    path('establishments/search/address/<str:address>/', EstablishmentAddressSearchAPIView.as_view(), name='establishment-address-search'),
    path('establishments/search/name/<str:name>/', EstablishmentNameSearchAPIView.as_view(), name='establishment-name-search'),
]