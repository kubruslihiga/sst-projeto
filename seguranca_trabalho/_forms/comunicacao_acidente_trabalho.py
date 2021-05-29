from django import forms
from seguranca_trabalho.submodels.funcionario import Funcionario

from seguranca_trabalho.submodels.comunicacao_acidente_trabalho import AvisoComunicacaoAcidente, ClassificacaoMedica, ComunicacaoAcidenteTrabalho, LadoCorpoAtingido, TipoAcidente, FatorAcidente, ParteCorpoAtingida, NaturezaLesao, TipoCAT, TipoInscricao, TipoLocalizacao

CLASSIFICACAO_MEDICA_OPTIONS =(
    (ClassificacaoMedica.NONE, "..."),
    (ClassificacaoMedica.CRM, "CRM"),
    (ClassificacaoMedica.CRO, "CRO"),
    (ClassificacaoMedica.RMS, "RMS")
)

LADO_CORPO_ATINGIDO_OPTIONS = (
    (LadoCorpoAtingido.NONE, "..."),
    (LadoCorpoAtingido.NAO_APLICA, "NÃO SE APLICA"),
    (LadoCorpoAtingido.ESQUERDA, "ESQUERDA"),
    (LadoCorpoAtingido.DIREITA, "DIREITA"),
    (LadoCorpoAtingido.AMBAS, "AMBAS")
)

TIPO_INSCRICAO_OPTIONS = (
    (TipoInscricao.NONE, "..."),
    (TipoInscricao.CNPJ, "CNPJ"),
    (TipoInscricao.CAEPF, "CAEPF"),
    (TipoInscricao.CNO, "CNO")
)

AVISO_COMUNICACAO_ACIDENTE_OPTIONS = (
    (AvisoComunicacaoAcidente.NONE, "..."),
    (AvisoComunicacaoAcidente.INICIATIVA_EMPREGADOR, "INICIATIVA DO EMPREGADOR"),
    (AvisoComunicacaoAcidente.ORDEM_JUDICIAL, "ORDEM JUDICIAL"),
    (AvisoComunicacaoAcidente.DETERMINACAO_ORGAO_FISCALIZADOR, "DETERMINAÇÃO DO ORGÃO FISCALIZADOR")
)

TIPO_CAT_OPTIONS = (
    (TipoCAT.NONE, "..."),
    (TipoCAT.INICIAL, "INICIAL"),
    (TipoCAT.REABERTURA, "REABERTURA"),
    (TipoCAT.COMUNICACAO_OBITO, "COMUNICAÇÃO DE ÓBITO")
)

TIPO_LOCALIZACAO_OPTIONS = (
    (TipoLocalizacao.NONE, "..."),
    (TipoLocalizacao.ESTABELECIMENTO_BRASIL, "ESTABELECIMENTO NO BRASIL"),
    (TipoLocalizacao.ESTABELECIMENTO_EXTERIOR, "ESTABELECIMENTO NO EXTERIOR"),
    (TipoLocalizacao.ESTABELECIMENTO_TERCEIROS, "ESTABELECIMENTO TERCEIROS"),
    (TipoLocalizacao.VIA_PUBLICA, "VIA PÚBLICA"),
    (TipoLocalizacao.AREA_RURAL, "ÁREA RURAL"),
    (TipoLocalizacao.EMBARCACAO, "EMBARCAÇÃO"),
    (TipoLocalizacao.OUTROS, "OUTROS"),
)

class ComunicacaoAcidenteTrabalhoForm(forms.ModelForm):
    tipo_cat = forms.ChoiceField(
        widget=forms.Select, 
        choices=TIPO_CAT_OPTIONS, 
        label="Tipo da CAT")
    acidente_aviso_comunicacao = forms.ChoiceField(
        widget=forms.Select, 
        choices=AVISO_COMUNICACAO_ACIDENTE_OPTIONS, 
        label="Comunicação do acidente")
    tipo_localizacao_acidente = forms.ChoiceField(
        widget=forms.Select, 
        choices=TIPO_LOCALIZACAO_OPTIONS, 
        label="Tipo do local do acidente")
    tipo_inscricao = forms.ChoiceField(
        widget=forms.Select, 
        choices=TIPO_INSCRICAO_OPTIONS, 
        label="Tipo de inscrição")
    lado_parte_corpo_atingida = forms.ChoiceField(
        widget=forms.Select, 
        choices=LADO_CORPO_ATINGIDO_OPTIONS, 
        label="Lado do corpo atingida")
    classificao_codigo_medico = forms.ChoiceField(
        widget=forms.Select, 
        choices=CLASSIFICACAO_MEDICA_OPTIONS, 
        label="Órgão de classe")
    acidente_data_hora = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(format="%d/%m/%Y %H:%M", attrs={ "data-mask": "99/99/9999 99:99" }), required=True, help_text="Formato dd/mm/yyyy HH:MM")
    acidente_data_obito = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(format="%d/%m/%Y %H:%M", attrs={ "data-mask": "99/99/9999 99:99" }), required=False, help_text="Formato dd/mm/yyyy HH:MM")

    def __init__(self, usuario, *args, **kwargs):
        super(ComunicacaoAcidenteTrabalhoForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset=Funcionario.objects.filter(empresa=usuario.empresa_selecionada)

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
            "internacao",
            "tempo_internacao",
            "afastamento_medico",
            "natureza_lesao",
            "lesao_complemento_descricao",
            "diagnostico",
            "cid_codigo",
            "atestado_medico_observacao",
            # informacao do profissional que emitiu atestado
            "nome_medico",
            "classificao_codigo_medico",
            "numero_inscricao_medica",
            "uf_medico",
            # numero CAT para reabertura
            "codigo_cat"]