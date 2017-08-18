# coding=utf-8
from django.forms import ModelForm
from .models import Ticket

__author__ = 'alexy'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('phone', 'email', 'theme', 'city')
