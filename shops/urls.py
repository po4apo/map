from rest_framework import routers
from .api import CityViewSet, StreetsInTheCurrentCityViewSet, CreateShop, ShopListViewSet
from django.urls import path, include, re_path

router = routers.DefaultRouter()


urlpatterns = [

    # path('city/', city_list),
    path('shop/', ShopListViewSet.as_view()),
    path('shop/', CreateShop.as_view()),
    path('city/<int:city_id>/street', StreetsInTheCurrentCityViewSet.as_view()),
    path('city/', CityViewSet.as_view()),
    path('', include(router.urls)),

]
