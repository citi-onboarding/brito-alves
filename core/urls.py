from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mail_sender', views.mail_sender, name='mail_sender'),
]