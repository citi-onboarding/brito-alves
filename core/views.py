from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.core.mail import send_mail

from core.models import Associado, AreaDeAtuacao, Institucional


def index(request):
    partners = Associado.objects.order_by('order')
    services = AreaDeAtuacao.objects.order_by('order')
    intitutional = Institucional.objects.all()

    context = {
        'main_services' : services[:3],
        'services' : services,
        'partners': partners,
        'intitutional' : intitutional[0] if len(intitutional) > 0 else '',
    }

    return render(request, 'index.html', context,)


def mail_sender(request):

    subject = '[SITE-CONTATO] ' + request.POST.get('subject')
    message = '<b>Nome:</b> ' + request.POST.get('name') + '<br>'
    message += '<b>E-mail:</b> ' + request.POST.get('email') + '<br><br>'
    message += '<b>Mensagem:</b> ' + request.POST.get('message')

    res = send_mail(
        subject,
        message,
        'balb.contact@gmail.com',
        ['balb.contact@gmail.com'],
        fail_silently=True,
        html_message=message,
    )

    response = redirect('index')

    if (res == 0):
        messages.error(request, 'Erro. Tente novamente mais tarde.')
    else:
        messages.success(request, 'Obrigado! Entraremos em contato assim que possível.')

    return response