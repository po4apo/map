from rest_framework import routers
from .api import city_list, add_shop, all_streets_in_the_current_city
from django.urls import path, include, re_path

router = routers.DefaultRouter()


urlpatterns = [
    path('city/', city_list),
    path('shop/', add_shop),
    path('city//<int:city_id>/', all_streets_in_the_current_city),
    path('', include(router.urls)),

]
