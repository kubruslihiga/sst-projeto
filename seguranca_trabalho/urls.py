from django.urls import path

from django.contrib.auth import views as auth_views
from seguranca_trabalho._views.equipamento import criar_equipamento, recuperar_equipamentos, detalhar_equipamento
from seguranca_trabalho._views.funcionario import criar_funcionario, detalhar_funcionario, recuperar_funcionarios
from seguranca_trabalho._views.funcionario_epi import associar_equipamento, associar_funcionario, recuperar_funcionario_epis, detalhar_funcionario_epi
from seguranca_trabalho._views.comunicacao_acidente_trabalho import criar_comunicacao_acidente_trabalho
from .views import criar_monitoramento_trabalhador, criar_condicao_fator_risco

urlpatterns = [
    path('comunicacao_acidente_trabalho/', criar_comunicacao_acidente_trabalho, name="comunicacao_acidente_trabalho"),
    path('monitoramento_saude_trabalhador/', criar_monitoramento_trabalhador, name="monitoramento_saude_trabalhador"),
    path('condicao_fator_risco/', criar_condicao_fator_risco, name="condicao_fator_risco"),
    path('equipamento/', recuperar_equipamentos, name="recuperar_equipamentos"),
    path('equipamento/novo', criar_equipamento, name="criar_equipamento"),
    path('equipamento/<int:id>/', detalhar_equipamento, name="detalhar_equipamento"),
    path('equipamento/<int:id>/funcionario', associar_funcionario, name="associar_funcionario"),
    path('funcionario/novo/', criar_funcionario, name="criar_funcionario"),
    path('funcionario/<int:id>/', detalhar_funcionario, name="detalhar_funcionario"),
    path('funcionario/<int:id>/equipamento', associar_equipamento, name="associar_equipamento"),
    path('funcionario/', recuperar_funcionarios, name="recuperar_funcionarios"),
    # path('funcionario_epi/novo/', criar_funcionario_epi, name="funcionario_epi"),
    path('funcionario_epi/<int:id>/', detalhar_funcionario_epi, name="detalhar_funcionario_epi"),
    path('funcionario_epi/', recuperar_funcionario_epis, name="recuperar_funcionario_epis"),
]