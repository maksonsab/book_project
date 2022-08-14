from typing import *

from django.contrib import admin
from django.db.models import QuerySet, Q

from .models import Book, Author

class YearFilter(admin.SimpleListFilter):
    parameter_name: str = 'year_filter'
    title: str = 'Периоды'
    
    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ('new', 'Современные'),
            ('20century', '20 Век'),
            ('old', 'Старые'),
            ('very_old', 'Древние книги')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet) -> Optional[QuerySet]:
        if self.value() == 'new':
            return queryset.filter(year__gte=2000)
        if self.value() == '20century':
            return queryset.filter(Q(year__gte=1900) & Q(year__lt=2000))
        if self.value() == 'old':
            return queryset.filter(Q(year__gte=1500) & Q(year__lt=1900))
        if self.value() == 'very_old':
            return queryset.filter(year__lt=1500)

class RatingFilter(admin.SimpleListFilter):
    parameter_name: str = 'rating_filter'
    title: str = 'Рейтинг'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ('top', 'Высочайший'),
            ('high', 'Высокий'),
            ('middle', 'Средний'),
            ('low', 'Низкий'),
        ]

    def queryset(self, request: Any, queryset: QuerySet) -> Optional[QuerySet]:
        if self.value() == 'top':
            return queryset.filter(rating__gte=90)
        if self.value() == 'high':
            return queryset.filter(Q(rating__lt=90) & Q(rating__gte=80))
        if self.value() == 'middle':
            return queryset.filter(Q(rating__lt=80) & Q(rating__gte=60))
        if self.value() == 'low':
            return queryset.filter(rating__lt=60)

#Admin classes
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'rating']
    list_filter: List = [YearFilter, RatingFilter]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_per_page: int = 10

