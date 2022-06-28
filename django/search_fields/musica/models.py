from django.db import models


class Genere(models.Model):
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'genere'
        verbose_name_plural = 'generi'
        ordering = ('nome', )

    def __str__(self):
        return self.nome


class Artista(models.Model):
    nome = models.CharField(max_length=256)
    is_gruppo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'artista'
        verbose_name_plural = 'artisti'
        ordering = ('nome', )

    def __str__(self):
        return self.nome


class Album(models.Model):
    titolo = models.CharField(max_length=256)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)

    anno_pubblicazione = models.IntegerField(null=True, blank=True)
    genere = models.ForeignKey(Genere, on_delete=models.SET_NULL, null=True,
            blank=True)

    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'album'
        ordering = ('titolo', )

    def __str__(self):
        return self.titolo
