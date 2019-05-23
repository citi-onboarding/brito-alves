from django.db import models
from django.db import models

class Associado(models.Model):
    name = models.CharField("Nome", max_length=30, null=False, blank=False)
    curriculum = models.CharField("Currículo", max_length=260, null=True, blank=True)
    image = models.ImageField("Imagem", null=False, blank=False)
    order = models.IntegerField("Ordem de exibição")

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Associado"
        verbose_name_plural = "Associados"

    def __str__(self):
        return self.name