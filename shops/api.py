from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from .filters import MyFilter
from .models import Shop, Street, City
from shops.serializers import ShopSerializer, StreetSerializer, CitySerializer
from .paginators import ResultsSetPagination


class CreateShop(CreateAPIView):
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(f'id:{(serializer.data["id"])}', status=status.HTTP_201_CREATED, headers=headers)


class ShopListViewSet(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [MyFilter]
    filterset_fields = ['street_id', 'city_id']
    pagination_class = ResultsSetPagination


class CityViewSet(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = ResultsSetPagination


class StreetsInTheCurrentCityViewSet(generics.ListAPIView):
    """
    Get list all streets in the current city.
    """
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    pagination_class = ResultsSetPagination

    def get(self, request, city_id = None, *args, **kwargs):
        self.queryset = self.get_queryset().filter(city_id=city_id)
        return self.list(request, *args, **kwargs)
