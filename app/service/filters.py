import django_filters

from .models import Events


class EventsFilter(django_filters.FilterSet):
    '''
        задание из ТЗ
         возможность фильтрации и сортировки по дате, поиском по названию
    '''

    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title')
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Events
        fields = ['title', 'date']
