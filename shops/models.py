from django.db import models


# Create your models here.


class Shop(models.Model):
    """Модель включает следующие поля:
        Название
        Город
        Улица
        Дом
        Время открытия
        maВремя закрытия"""
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Название магазина'
                            )
    num_of_house = models.CharField(max_length=10,
                                    verbose_name='Номер дома',
                                    )
    opening_time = models.TimeField(max_length='Время открытия',
                                    )
    closing_time = models.TimeField(max_length='Время открытия',
                                    )
    street = models.ForeignKey('Street',
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='Улица',
                               )
    city = models.ForeignKey('City',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name='Город',
                             )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Street(models.Model):
    """Модель включает следующие поля:
    Название
    Город
    """
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Название улицы'
                            )

    city = models.ForeignKey('City',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name='Город',
                             )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class City(models.Model):
    """Модель включает следующие поля:
    Название
    """
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Название города',
                            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
