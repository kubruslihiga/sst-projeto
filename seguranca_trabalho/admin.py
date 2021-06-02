from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from seguranca_trabalho.submodels.comunicacao_acidente_trabalho import *
from seguranca_trabalho.submodels.monitoramento_saude_trabalhador import *
from seguranca_trabalho.submodels.empresa import *
from seguranca_trabalho.submodels.funcionario import *
from seguranca_trabalho.submodels.equipamento import *
from seguranca_trabalho.submodels.condicao_fator_risco_ambiente_trabalho import *
from seguranca_trabalho.submodels.usuario import Usuario


admin.site.register(Usuario)

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Funcao)
admin.site.register(ClassificacaoBrasileiraOcupacao)

admin.site.register(Equipamento)
admin.site.register(FuncionarioEquipamento)

admin.site.register(ComunicacaoAcidenteTrabalho)
admin.site.register(FatorAcidente)
admin.site.register(NaturezaLesao)
admin.site.register(ParteCorpoAtingida)
admin.site.register(TipoAcidente)

admin.site.register(MedicoASO)
admin.site.register(Procedimento)
admin.site.register(MonitoramentoSaudeTrabalhador)

admin.site.register(Atividade)
admin.site.register(FatorRisco)
admin.site.register(UnidadeMedida)
admin.site.register(ResponsavelRegistroAmbiental)
admin.site.register(AnaliseEPI)
admin.site.register(CondicaoFatorRisco)