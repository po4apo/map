
from rest_framework import serializers

from .models import Shop, Street, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ["name", "num_of_house", "opening_time","closing_time","street","city","open"]

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must be str")
        return value


class ShopSerializerDetal(serializers.ModelSerializer):
    city = serializers.StringRelatedField(read_only=True)
    street =  serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'num_of_house', 'opening_time', 'closing_time', 'street', 'city', 'open']


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'
