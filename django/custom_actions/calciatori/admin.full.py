import csv

from django.contrib import admin, messages
from django.http import HttpResponse

from .models import Calciatore


def esport_csv_generica(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=generico.csv'
    writer = csv.writer(response)
    
    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response
esport_csv_generica.short_description = 'Esporta selezione su csv (generico)'
    

class EsportaCsvMixin:
    def esporta_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        

        return response
    esporta_csv.short_description = 'Esporta selezione su csv'


def contrattualizza(modeladmin, request, queryset):
    contrattualizzati = queryset.update(status=Calciatore.CON_CONTRATTO)
    modeladmin.message_user(request, 
        f"Contrattualizzati {contrattualizzati} calciatori.", 
        messages.SUCCESS
    )


class ContrattualizzaMixin:
    def contrattualizza_calciatore(self, request, queryset):
        contrattualizzati = queryset.update(status=Calciatore.CON_CONTRATTO)
        self.message_user(request, 
            f"Contrattualizzati {contrattualizzati} calciatori.", 
            messages.SUCCESS
        )
    contrattualizza_calciatore.short_description = "Contrattualizza"


@admin.register(Calciatore)
class CalciatoreAdmin(admin.ModelAdmin, ContrattualizzaMixin):
    list_display = ['nome', 'ruolo', 'squadra', 'status']
    list_filter = ('ruolo', 'squadra', 'status')
    # actions = ['esporta_csv', esport_csv_generica, contrattualizza]
    actions = ['contrattualizza_calciatore']
