from django.db import models


class Calciatore(models.Model):
    PORTIERE = 'P'
    DIFENSORE = 'D'
    CENTROCAMPISTA = 'C'
    ATTACCANTE = 'A'
    RUOLI_CHOICES = [
        (PORTIERE, 'portiere'),
        (DIFENSORE, 'difensore'),
        (CENTROCAMPISTA, 'centrocampista'),
        (ATTACCANTE, 'attaccante'),
    ]

    SVINCOLATO = 0
    CON_CONTRATTO = 1
    STATUS_CHOICES = [
        (SVINCOLATO, 'svincolato'),
        (CON_CONTRATTO, 'con_contratto')
    ]

    nome = models.CharField(max_length=256)
    ruolo = models.CharField(max_length=1, choices=RUOLI_CHOICES)
    squadra = models.CharField(max_length=256)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
            default=SVINCOLATO)

    class Meta:
        verbose_name = 'calciatori'
        verbose_name_plural = 'calciatori'

    def __str__(self):
        return self.nome
