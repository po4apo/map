from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from shops.models import Shop, Street, City
from shops.serializers import ShopSerializer, StreetSerializer, CitySerializer, ShopSerializerDetal


@api_view(['GET'])
def city_list(request):
    """
    List all cities.
    """
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def all_streets_in_the_current_city(request, city_id):
    """
    List all streets in the current city.
    """
    try:
        streets = Street.objects.filter(city_id=city_id)
    except Street.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def add_shop(request):
    """
    List shops filtered on params.
    If param isn't valid then this param is ignored.


    Example JSON for POST:
    {
    "name":"Магнит",
    "num_of_house": 30,
    "opening_time": "04:00:00",
    "closing_time": "20:00:00",
    "street": 1,
    "city": 2
    }
    """
    try:
        # ?street=&city=&open=0/1
        # get_params
        params = {'street_id': request.GET.get('street', None),
                  'city_id': request.GET.get('city', None),
                  }
        user_param_for_field_open = request.GET.get('open')
        # normalize_data
        valid_params = {k: v for k, v in params.items() if (v is not None and v.isdigit())}
        # get_data_from_db
        shops = Shop.objects.filter(**valid_params)
        if user_param_for_field_open is not None and user_param_for_field_open.isdigit():
            shops = [x for x in shops if (x.open == int(user_param_for_field_open))]

    except Shop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopSerializerDetal(shops, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
