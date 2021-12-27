import datetime

from django.db.models import F, Q
from django.utils.timezone import now
from django_filters import utils
from django_filters.rest_framework import DjangoFilterBackend


class MyFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        print(queryset)
        print(filterset.qs)
        if request.GET.get('open') is not None and request.GET.get('open').isdigit():
            if int(request.GET.get('open')):
                queryset = queryset.filter(opening_time__lte = datetime.datetime.now().time(),
                                           closing_time__gte = datetime.datetime.now().time())
            else:
                queryset = queryset.filter(Q(opening_time__gte = datetime.datetime.now().time()) |
                                           Q(closing_time__lte = datetime.datetime.now().time()))

        print(queryset)
        print(filterset.qs)

        if filterset is None:
            return queryset

        if not filterset.is_valid() and self.raise_exception:
            raise utils.translate_validation(filterset.errors)

        return queryset


