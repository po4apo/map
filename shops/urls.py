from rest_framework import routers
from .api import CityViewSet, StreetsInTheCurrentCityViewSet, ShopListViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('shop', ShopListViewSet)


urlpatterns = [
    path('city/<int:city_id>/street', StreetsInTheCurrentCityViewSet.as_view()),
    path('city/', CityViewSet.as_view()),
    path('', include(router.urls)),

]
