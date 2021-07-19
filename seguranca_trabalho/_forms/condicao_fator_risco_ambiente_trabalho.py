from seguranca_trabalho.submodels.funcionario import Funcionario
from django import forms
from django.forms.models import BaseInlineFormSet, inlineformset_factory

from seguranca_trabalho.submodels.monitoramento_saude_trabalhador import MonitoramentoSaudeTrabalhador
from seguranca_trabalho.submodels.usuario import Usuario
from seguranca_trabalho.submodels.condicao_fator_risco_ambiente_trabalho import CondicaoAmbientalFatorRisco, CondicaoFator, AnaliseEPI

class CondicaoAmbientalFatorRiscoForm(forms.ModelForm):
    usuario:Usuario
    def __init__(self, usuario:Usuario, *args, **kwargs):
        super(CondicaoAmbientalFatorRiscoForm, self).__init__(*args, **kwargs)
        self.usuario = usuario
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=usuario.empresa_selecionada)

    data_inicio = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        widget=forms.DateInput(
            format="%d/%m/%Y", 
            attrs={ "data-mask": "99/99/9999" }), 
            required=False,
            help_text="Formato dd/mm/yyyy")
    funcionario = forms.ModelChoiceField(queryset=None, required=True, label="Funcionário", widget=forms.Select(attrs={
        "class": "select"
    }))
    responsavel_registro_ambiental = forms.ModelChoiceField(queryset=None, label="Responsável pelo registro", required=False)
    descricao_atividade_ambiente = forms.CharField(required=False, label="Descrição da atividade no ambiente de trabalho")
    metodologia_riscos_ergonomicos = forms.CharField(required=False, label="Metodologia dos riscos ergonômicos", max_length=1000, widget=forms.Textarea())
    observacao = forms.CharField(required=False, label="Observação", max_length=1000, widget=forms.Textarea())

    class Meta:
        model = CondicaoAmbientalFatorRisco
        fields = ["funcionario",
                "data_inicio",
                "descricao_atividade_ambiente",
                "atividades",
                "responsavel_registro_ambiental",
                "metodologia_riscos_ergonomicos",
                "observacao"]

class BaseCondicaoAmbiente(BaseInlineFormSet):
    def add_fields(self, form, index) -> None:
        super().add_fields(form, index)

class CondicaoFatorForm(forms.ModelForm):
    class Meta:
        model = CondicaoFator
        fields = [
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
            "utilizacao_epi"]

class AnaliseEPIForm(forms.ModelForm):
    class Meta:
        model = AnaliseEPI
        fields = [
            "certificacao_epi",
            "descricao_epi",
            "epi_eficaz",
            "hierarquia_medida_protecao_coletiva",
            "observada_condicao_funcionamento",
            "observado_epi",
            "observado_prazo_validade_ca",
            "observado_periodicidade_troca",
            "observada_higienizacao_epi"]

AnaliseEPIFormset = inlineformset_factory(CondicaoFator, AnaliseEPI, form=AnaliseEPIForm, extra=1)

class BaseCondicaoFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseCondicaoFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.analise_epis = AnaliseEPIFormset(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='analise-epi-%s-%s' % (
                            form.prefix,
                            AnaliseEPIFormset.get_default_prefix()))

CondicaoFatorFormset = inlineformset_factory(CondicaoAmbientalFatorRisco, CondicaoFator, form=CondicaoFatorForm, formset=BaseCondicaoFormset, extra=1)