from django.shortcuts import render
from django.views.generic import ListView

from pessoa.models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')
