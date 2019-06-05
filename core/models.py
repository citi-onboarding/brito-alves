from django.db import models


class AreaDeAtuacao(models.Model):
    title = models.CharField("Título", max_length=25)
    description = models.CharField("Descrição rápida", max_length=80)
    text = models.TextField("Texto sobre a área")
    image = models.ImageField("Imagem", upload_to="area_atuacao/", null=True, blank=True)
    order = models.IntegerField("Ordem de exibição")

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Área de atuação"
        verbose_name_plural = "Áreas de atuação"

    def __str__(self):
        return self.title


class Associado(models.Model):
    name = models.CharField("Nome", max_length=30, null=False, blank=False)
    curriculum = models.CharField("Currículo", max_length=260, null=True, blank=True)
    image = models.ImageField("Imagem", upload_to="associado/", null=False, blank=False)
    order = models.IntegerField("Ordem de exibição")

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Associado"
        verbose_name_plural = "Associados"

    def __str__(self):
        return self.name


class Institucional(models.Model):
    text = models.TextField("Texto sobre a empresa")

    class Meta:
        verbose_name = "Institucional"
        verbose_name_plural = "Institucional"

    def __str__(self):
        return self.text