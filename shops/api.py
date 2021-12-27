from rest_framework import generics
from rest_framework.viewsets import GenericViewSet

from .serializers import ShopSerializer, StreetSerializer, CitySerializer
from .filters import MyFilter
from .models import Shop, Street, City
from .paginators import ResultsSetPagination


class ShopListViewSet(GenericViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Shop.objects.all().order_by('name')
    serializer_class = ShopSerializer
    filter_backends = [MyFilter]
    filterset_fields = ['street_id', 'city_id']
    pagination_class = ResultsSetPagination


class CityViewSet(generics.ListAPIView):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer
    pagination_class = ResultsSetPagination


class StreetsInTheCurrentCityViewSet(generics.ListAPIView):
    """
    Get list all streets in the current city.
    """
    queryset = Street.objects.all().order_by('name')
    serializer_class = StreetSerializer
    pagination_class = ResultsSetPagination

    def get(self, request, city_id=None, *args, **kwargs):
        self.queryset = self.get_queryset().filter(city_id=city_id)
        return self.list(request, *args, **kwargs)
