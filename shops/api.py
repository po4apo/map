from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from shops.models import Shop, Street, City
from shops.serializers import ShopSerializer, StreetSerializer, CitySerializer


def city_list(request):
    """
    List all cities, or create a new city.
    """
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def all_streets_in_the_current_city(request, city_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        streets = Street.objects.filter(city_id=city_id)
    except Street.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StreetSerializer(streets, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StreetSerializer(streets, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        streets.delete()
        return HttpResponse(status=204)