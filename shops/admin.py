from django.contrib import admin
from .models import City, Street, Shop


class AdminCity(admin.ModelAdmin):
    list_display = ('name', )


class AdminStreet(admin.ModelAdmin):
    list_display = ('name', 'city')


class AdminShop(admin.ModelAdmin):
    list_display = ('name', 'num_of_house', 'opening_time', 'closing_time', 'city', 'street')


admin.site.register(City, AdminCity)
admin.site.register(Street, AdminStreet)
admin.site.register(Shop, AdminShop)