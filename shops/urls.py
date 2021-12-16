from rest_framework import routers
from .api import CityViewSet, StreetsInTheCurrentCityViewSet, CreateShop, ShopListViewSet
from django.urls import path, include, re_path

router = routers.DefaultRouter()
router.register(r'city', CityViewSet, basename='city')


urlpatterns = [

    # path('city/', city_list),
    path('shop/', ShopListViewSet.as_view()),
    path('shop/', CreateShop.as_view()),
    path('city/<int:city_id>/street', StreetsInTheCurrentCityViewSet.as_view({'get': 'list'})),

    path('', include(router.urls)),

]
