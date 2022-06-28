from django.contrib import admin

from musica.models import Genere, Artista, Album


@admin.register(Genere)
class GenereAdmin(admin.ModelAdmin):
    pass


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'is_gruppo')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'artista', 'anno_pubblicazione')
    search_fields = ['titolo', 'artista__nome']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = \
                super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term) + 10
        except ValueError:
            pass
        else:
            queryset |= \
                self.model.objects.filter(anno_pubblicazione=search_term_as_int)
        return queryset, use_distinct

