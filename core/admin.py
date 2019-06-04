from django.contrib import admin
from core.models import AreaDeAtuacao, Associado, Institucional


@admin.register(AreaDeAtuacao)
class AreaDeAtuacaoAdmin(admin.ModelAdmin):
    list_display = ("title", "order",)


@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ("name", "order",)

@admin.register(Institucional)
class InstitucionalAdmin(admin.ModelAdmin):
    list_display = ("text",)
