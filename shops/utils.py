import os

from django.db import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'map.settings')
import django

django.setup()
from shops.models import Shop, City, Street
from requests import request

url = 'http://kladr-api.ru/api.php'


def add_city_in_model():
    name = input('Введите название города:').lower().capitalize()
    city = City.objects.create(name=name)
    print(f'Добавлен город:{city.name}')
    return city.name, city.id


def add_street_in_model(name, city_id):
    street = Street.objects.create(name=name, city_id=city_id)
    print(f'Добавлена улица:{street.name}')


def get_cities_from_model():
    qs = City.objects.all()
    print('\nВыбирите id города, или напишите 0 для добавления нового:')
    for obj in qs:
        print(f'{obj.id}-{obj.name}')
    num = int(input())
    if num == 0:
        return add_city_in_model()
    city = qs.filter(pk=num)[0]
    return city.name, city.id


def get_street(city, street):
    """
    Gets street from Internet, then adds street in model
    """
    response_city = request(url=url,
                            method='GET',
                            params={
                                'query': city[0],
                                'contentType': 'city'
                            }).json()

    response_street = request(url=url,
                              method='GET',
                              params={
                                  'query': street,
                                  'contentType': 'street',
                                  'cityId': response_city['result'][1]['id']
                              }).json()

    add_street_in_model(response_street['result'][1]['name'], city[1])
    return response_street


def get_streets(city):
    """
    Gets all street for city from Internet, then adds streets in model
    """
    print('start find city')
    response_city = request(url=url,
                            method='GET',
                            params={
                                'query': city[0],
                                'contentType': 'city'
                            }).json()
    print(f'city:{response_city}')
    response_street = request(url=url,
                              method='GET',
                              params={
                                  'contentType': 'street',
                                  'cityId': response_city['result'][1]['id'],
                              }).json()
    print(f'street:{response_street}')
    for street in response_street['result'][1:]:
        print(street['name'])
        try:
            add_street_in_model(street['name'], city[1])
        except IntegrityError:
            print('Такое имя уже есть')
    return response_street


if __name__ == '__main__':
    while True:
        city = get_cities_from_model()

        print(
            '\nВыбирите номер действия:\n1.Добавить конкретную улицу в этом городе\n2.Добавить все улицы этого города\n3.Выйти')
        num = int(input())
        if num == 3:
            break
        elif num == 1:
            street = input('Введите название улицы:').lower().capitalize()
            get_street(city, street)
        elif num == 2:
            get_streets(city)
