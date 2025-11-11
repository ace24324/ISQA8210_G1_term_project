
from django_filters import FilterSet, ChoiceFilter
from .models import Listing

RANGE_CHOICES = [
    ('0-49999', '0 to 49999'),
    ('50000-99999', '50000 to 99999'),
    ('100000-149999', '100000 to 149999'),
    ('150000-199999', '150000 to 199999'),
    ('200000-249999', '200000 to 249999'),
    ('250000-299999', '250000 to 299999'),
    ('300000-349999', '300000 to 349999'),
    ('350000-99999999', '350000 to 99999999'),
]

class ListingFilter(FilterSet):
    range_filter = ChoiceFilter(
        choices=RANGE_CHOICES,
        method='filter_by_range',
        label='Price Range',
    )

    class Meta:
        model = Listing
        fields = ['type', 'prop_neighborhood']

    def filter_by_range(self, queryset, name, value):
        if value == '0-49999':
            return queryset.filter(price__gte=0, price__lte=49999)
        elif value == '50000-99999':
            return queryset.filter(price__gte=50000, price__lte=99999)
        elif value == '100000-149999':
            return queryset.filter(price__gte=100000, price__lte=149999)
        elif value == '150000-1999999':
            return queryset.filter(price__gte=150000, price__lte=199999)
        elif value == '200000-249999':
            return queryset.filter(price__gte=200000, price__lte=249999)
        elif value == '250000-299999':
            return queryset.filter(price__gte=250000, price__lte=299999)
        elif value == '300000-349999':
            return queryset.filter(price__gte=300000, price__lte=349999)
        elif value == '350000-99999999':
            return queryset.filter(price__gte=350000, price__lte=99999999)
        return queryset
