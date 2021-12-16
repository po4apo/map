from django.contrib import admin
from .models import City, Street, Shop


class AdminCity(admin.ModelAdmin):
    list_display = ('pk','name', )


class AdminStreet(admin.ModelAdmin):
    list_display = ('name', 'city', )
    list_filter = ('city', )


class AdminShop(admin.ModelAdmin):
    list_display = ('name', 'num_of_house', 'opening_time', 'closing_time', 'city', 'street', )
    list_filter = ('street', 'city', )
    list_editable = ('opening_time', 'closing_time',)


admin.site.register(City, AdminCity)
admin.site.register(Street, AdminStreet)
admin.site.register(Shop, AdminShop)