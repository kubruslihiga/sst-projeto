# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm

from seguranca_trabalho.submodels.comunicacao_acidente_trabalho import ComunicacaoAcidenteTrabalho, TipoAcidente, FatorAcidente, ParteCorpoAtingida, NaturezaLesao
from seguranca_trabalho.submodels.monitoramento_saude_trabalhador import MonitoramentoSaudeTrabalhador
from seguranca_trabalho.submodels.condicao_fator_risco_ambiente_trabalho import CondicaoFatorRisco

class MonitoramentoSaudeTrabalhadorForm(forms.ModelForm):
    class Meta:
        model = MonitoramentoSaudeTrabalhador
        fields = ["estagiario",
                    "tipo_exame",
                    "data_aso",
                    "resultado_aso",
                    "data_exame",
                    "procedimento",
                    "observacao_procedimento",
                    "ordem_exame",
                    "indicacao_resultado",
                    "medicos",
                    "coordenador_cpf",
                    "coordenador_crm",
                    "coordenador_uf",
                    "coordenador_nome"]

class CondicaoFatorRiscoForm(forms.ModelForm):
    class Meta:
        model = CondicaoFatorRisco
        fields = ["funcionario",
                "data_inicio",
                "descricao_atividade_ambiente",
                "atividades",
                "fator_risco",
                "tipo_avaliacao",
                "intensidade",
                "limite_tolerancia",
                "unidade_medida",
                "tecnica_utilizada",
                "insalubridade",
                "periculosidade",
                "aposentadoria_especial",
                "utilizacao_epc",
                "epc_eficaz",
                "utilizacao_epi",
                "analises_epi",
                "responsaveis_registro_ambiental",
                "metodologia_riscos_ergonomicos",
                "observacao"]
