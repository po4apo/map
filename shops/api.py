from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view

from .filters import MyFilter
from .models import Shop, Street, City
from shops.serializers import ShopSerializer, StreetSerializer, CitySerializer, ShopSerializerDetal
from django_filters.rest_framework import DjangoFilterBackend



class CityViewSet(viewsets.ViewSet):
    # todo: Добавить пагинацию
    def list(self, request):
        """
        Get list with cities
        """
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


class StreetsInTheCurrentCityViewSet(viewsets.ViewSet):
    """
    Get list all streets in the current city.
    """
    def list(self, request, city_id = None):
        streets = Street.objects.filter(city_id=city_id)
        if streets.exists():
            serializer = StreetSerializer(streets, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateShop(CreateAPIView):
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(f'id:{(serializer.data["id"])}', status=status.HTTP_201_CREATED, headers=headers)


# class ShopListViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         print(request.GET)
#         params = {'street__id': request.GET.get('street', None),
#                   'city_id': request.GET.get('city', None),
#         }
#         streets = Shop.objects.filter(**params)
#         if streets.exists():
#             serializer = StreetSerializer(streets, many=True)
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


class ShopListViewSet(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [MyFilter]
    filterset_fields = ['street_id', 'city_id']