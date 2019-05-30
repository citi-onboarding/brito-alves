from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from core.models import Associado, AreaDeAtuacao


def index(request):
    partners = Associado.objects.order_by('order')
    services = AreaDeAtuacao.objects.order_by('order')
    context = {
        'main_services' : services[:3],
        'services' : services,
        'partners': partners
    }
    return render(request, 'index.html', context)