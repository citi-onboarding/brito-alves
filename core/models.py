from django.db import models


class AreaDeAtuacao(models.Model):
    title = models.CharField("Título", max_length=25)
    description = models.CharField("Descrição rápida", max_length=80)
    text = models.TextField("Texto sobre a área")
    image = models.ImageField("Imagem", null=True, blank=True)
    order = models.IntegerField("Ordem de exibição")

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Área de atuação"
        verbose_name_plural = "Áreas de atuação"

    def __str__(self):
        return self.title
