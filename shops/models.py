import datetime
from django.db.models import Func, F

from django.db import models


# Create your models here.


class NewManager(models.Manager):

    def get_queryset(self):
        """Overrides the models.Manager method"""
        qs = (super(NewManager, self).get_queryset()).annotate(open = F('name'))
        print(list(qs))
        return qs


class Shop(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Название магазина'
                            )
    num_of_house = models.CharField(max_length=10,
                                    verbose_name='Номер дома',
                                    )
    opening_time = models.TimeField(verbose_name='Время открытия',
                                    )
    closing_time = models.TimeField(verbose_name='Время закрытия',
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



    @property
    def open(self):
        print(self.opening_time)
        print(self.closing_time)
        print(datetime.datetime.now().time())
        return int(self.opening_time < datetime.datetime.now().time() < self.closing_time)



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
