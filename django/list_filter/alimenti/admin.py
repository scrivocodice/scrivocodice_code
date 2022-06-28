from django.contrib import admin
from alimenti.models import Tipologia, Alimento


class CalorieListFilter(admin.SimpleListFilter):
    title = "Calorie"
    parameter_name = 'calories'

    DIETETICO = "1"
    NORMALE = "2"
    CALORICO = "3"

    def lookups(self, request, model_admin):
        return (
            (self.DIETETICO, "dietetico"),
            (self.NORMALE, "normale"),
            (self.CALORICO, "calorico"),
        )

    def queryset(self, request, queryset):
        if self.value() == self.DIETETICO:
            return queryset.filter(calorie__lt=100)
        if self.value() == self.NORMALE:
            return queryset.filter(calorie__gte=100,calorie__lt=200)
        if self.value() == self.CALORICO:
            return queryset.filter(calorie__gte=200)


@admin.register(Tipologia)
class TipologiaAdmin(admin.ModelAdmin):
    pass


@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipologia', 'calorie']
    list_filter = ()
    list_filter = [
        'calorie', 
        CalorieListFilter,
        ('tipologia', admin.RelatedOnlyFieldListFilter),
        ('is_vegetale', admin.BooleanFieldListFilter),
    ]


