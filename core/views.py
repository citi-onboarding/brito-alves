from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from core.models import Associado


def index(request):
    partners = Associado.objects.all()
    return render(request, 'index.html', {'partners': partners})
