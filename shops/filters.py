from datetime import datetime

from django.db.models import F
from django_filters import utils
from django_filters.rest_framework import DjangoFilterBackend


class MyFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)

        if request.GET.get('open') is not None and request.GET.get('open').isdigit():
            print('in if')
            queryset = [x for x in queryset if (x.open == int(request.GET.get('open')))]
            print('end if', queryset)

        # if filterset is None:
        return queryset

        # if not filterset.is_valid() and self.raise_exception:
        #     raise utils.translate_validation(filterset.errors)
        # return filterset.qs


