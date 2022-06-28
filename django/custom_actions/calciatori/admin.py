import csv

from django.contrib import admin, messages
from django.http import HttpResponse

from .models import Calciatore


def contrattualizza(modeladmin, request, queryset):
    num_items = queryset.update(status=Calciatore.CON_CONTRATTO)
    modeladmin.message_user(
        request,
        f"Contrattualizzati {num_items} calciatori.",
        messages.SUCCESS
    )

class ContrattualizzaMixin:
    def contrattualizza_calciatore(self, request, queryset):
        num_items = queryset.update(status=Calciatore.CON_CONTRATTO)
        self.message_user(
            request,
            f"Contrattualizzati {num_items} calciatori.",
            messages.SUCCESS
        )
    contrattualizza_calciatore.short_description = 'Contrattualizza da classe'


@admin.register(Calciatore)
class CalciatoreAdmin(admin.ModelAdmin, ContrattualizzaMixin):
    list_display = ['nome', 'ruolo', 'squadra', 'status']
    list_filter = ('ruolo', 'squadra', 'status')
    actions = [contrattualizza, 'contrattualizza_calciatore']
