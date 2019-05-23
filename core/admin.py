from django.contrib import admin
from core.models import Associado

@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ("name", "order",)