# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm

from seguranca_trabalho.submodels.comunicacao_acidente_trabalho import ComunicacaoAcidenteTrabalho, TipoAcidente, FatorAcidente, ParteCorpoAtingida, NaturezaLesao
from seguranca_trabalho.submodels.monitoramento_saude_trabalhador import MonitoramentoSaudeTrabalhador
from seguranca_trabalho.submodels.condicao_fator_risco_ambiente_trabalho import CondicaoFatorRisco

class ComunicacaoAcidenteTrabalhoForm(forms.ModelForm):
    class Meta:
        model = ComunicacaoAcidenteTrabalho
        fields = ["acidente_data_hora", "tipo_acidente", "tipo_cat", "acidente_horas_trabalhadas",
                    "acidente_obito", "acidente_data_obito", "acidente_notificacao_policial", "fator_acidente",
                    "acidente_aviso_comunicacao", "observacao", "tipo_localizacao_acidente", 
                    "localizacao_acidente_especificacao", "acidente_tipo_endereco", "acidente_endereco_descricao",
                    "acidente_endereco_numero", "acidente_endereco_complemento", "acidente_endereco_bairro",
                    "acidente_endereco_cep", "acidente_endereco_cidade", "acidente_endereco_estado",
                    "acidente_endereco_pais", "acidente_endereco_codigo_postal", "tipo_inscricao",
                    "inscricao_numero", "parte_corpo_atingida", "lado_parte_corpo_atingida",
                    "atestado_medico_codigo", "atestado_medico_data", "hospital", "tempo_hospital",
                    "afastamento_medico", "natureza_lesao", "lesao_complemento_descricao", "diagnostico",
                    "cid_codigo", "atestado_medico_observacao", "nome_medico", "natureza_lesao_classificao",
                    "classificao_codigo_medico", "uf_medico", "codigo_cat"]

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
