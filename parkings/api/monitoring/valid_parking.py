import django_filters
import rest_framework_gis.pagination as gis_pagination
from django.utils.translation import ugettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ...models import Parking
from ..common import WGS84InBBoxFilter
from .permissions import MonitoringApiPermission
from .serializers import ParkingSerializer


class ValidParkingFilter(django_filters.rest_framework.FilterSet):
    time = django_filters.IsoDateTimeFilter(
        name='time', label=_("Time"), method='filter_time', required=True)

    class Meta:
        model = Parking
        fields = [
            'time',
            'region',
            'zone',
        ]
        strict = django_filters.STRICTNESS.RAISE_VALIDATION_ERROR

    def filter_time(self, queryset, name, value):
        return queryset.valid_at(value)


class ValidParkingViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [MonitoringApiPermission]
    queryset = (
        Parking.objects
        .order_by('time_start')
        .select_related('operator'))
    serializer_class = ParkingSerializer
    pagination_class = gis_pagination.GeoJsonPagination
    filter_class = ValidParkingFilter
    bbox_filter_field = 'location'
    filter_backends = [DjangoFilterBackend, WGS84InBBoxFilter]
    bbox_filter_include_overlapping = True
