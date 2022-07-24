from django.urls import URLPattern, path
from .views import ListaPessoaView


urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoa.index')
]