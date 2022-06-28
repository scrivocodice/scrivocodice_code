from django.db import models



class Tipologia(models.Model):
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'tipologia'
        verbose_name_plural = 'tipologie'
        ordering = ('nome', )

    def __str__(self):
        return self.nome


class Alimento(models.Model):
    nome = models.CharField(max_length=256)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.PROTECT)
    calorie = models.IntegerField()

    is_vegetale = models.BooleanField(default=False)
    is_animale = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'alimento'
        verbose_name_plural = 'alimenti'
        ordering = ('nome', )

    def __str__(self):
        return self.nome
