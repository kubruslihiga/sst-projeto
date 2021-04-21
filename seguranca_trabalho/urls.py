from django.urls import path

from django.contrib.auth import views as auth_views
from seguranca_trabalho._views.equipamento import criar_equipamento
from seguranca_trabalho._views.funcionario import criar_funcionario, detalhar_funcionario, recuperar_funcionarios
from seguranca_trabalho._views.funcionario_epi import criar_funcionario_epi, recuperar_funcionario_epis, detalhar_funcionario_epi
from .views import criar_cat, criar_monitoramento_trabalhador, criar_condicao_fator_risco

urlpatterns = [
    path('comunicacao_acidente_trabalho/', criar_cat, name="comunicacao_acidente_trabalho"),
    path('monitoramento_saude_trabalhador/', criar_monitoramento_trabalhador, name="monitoramento_saude_trabalhador"),
    path('condicao_fator_risco/', criar_condicao_fator_risco, name="condicao_fator_risco"),
    path('epi/', criar_equipamento, name="equipamento"),
    path('funcionario/novo/', criar_funcionario, name="funcionario"),
    path('funcionario/<int:id>/', detalhar_funcionario, name="detalhar_funcionario"),
    path('funcionario/', recuperar_funcionarios, name="recuperar_funcionarios"),
    path('funcionario_epi/novo/', criar_funcionario_epi, name="funcionario_epi"),
    path('funcionario_epi/<int:id>/', detalhar_funcionario_epi, name="detalhar_funcionario_epi"),
    path('funcionario_epi/', recuperar_funcionario_epis, name="recuperar_funcionario_epis"),
]