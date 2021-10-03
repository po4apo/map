from rest_framework import routers
from .api import city_list, all_streets_in_the_current_city
from django.urls import path, include

router = routers.DefaultRouter()


urlpatterns = [
    path('city/', city_list),
    path('city//<int:city_id>/', all_streets_in_the_current_city),
    path('', include(router.urls)),

]
