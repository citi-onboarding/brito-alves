from django.contrib import admin
from core.models import Associado

# Register your models here.
@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ("name", "order",)
