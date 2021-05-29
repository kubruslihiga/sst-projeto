from django import forms

from seguranca_trabalho.submodels.comunicacao_acidente_trabalho import ComunicacaoAcidenteTrabalho, TipoAcidente, FatorAcidente, ParteCorpoAtingida, NaturezaLesao

class ComunicacaoAcidenteTrabalhoForm(forms.ModelForm):
    class Meta:
        model = ComunicacaoAcidenteTrabalho
        fields = [
            "funcionario",
            # informacao sobre a comunicacao
            "acidente_data_hora",
            "tipo_acidente",
            "acidente_horas_trabalhadas",
            "tipo_cat",
            "acidente_obito",
            "acidente_data_obito",
            "acidente_notificacao_policial",
            "fator_acidente",
            "acidente_aviso_comunicacao",
            "observacao",
            # local
            "tipo_localizacao_acidente",
            "localizacao_acidente_especificacao",
            "acidente_tipo_endereco",
            "acidente_endereco_descricao",
            "acidente_endereco_numero",
            "acidente_endereco_complemento",
            "acidente_endereco_bairro",
            "acidente_endereco_cep",
            "acidente_endereco_pais",
            "acidente_endereco_estado",
            "acidente_endereco_cidade",
            "acidente_endereco_codigo_postal",
            # identificacao do local onde ocorreu o acidente
            "tipo_inscricao",
            "inscricao_numero",
            # detalhamento parte corpo acidente
            "parte_corpo_atingida",
            "lado_parte_corpo_atingida",
            # agentes causadores da CAT
            "agentes_causadores",
            # atestado médico
            "atestado_medico_codigo",
            "atestado_medico_data",
            "hospital",
            "tempo_hospital",
            "afastamento_medico",
            "natureza_lesao",
            "lesao_complemento_descricao",
            "diagnostico",
            "cid_codigo",
            "atestado_medico_observacao",
            # informacao do profissional que emitiu atestado
            "nome_medico",
            "natureza_lesao_classificao",
            "classificao_codigo_medico",
            "uf_medico",
            # numero CAT para reabertura
            "codigo_cat"]