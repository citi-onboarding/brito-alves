from django.contrib import admin
from core.models import AreaDeAtuacao


@admin.register(AreaDeAtuacao)
class AreaDeAtuacaoAdmin(admin.ModelAdmin):
    list_display = ("title", "order",)
