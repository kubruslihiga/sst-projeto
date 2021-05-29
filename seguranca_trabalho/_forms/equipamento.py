
from django import forms

from seguranca_trabalho.submodels.equipamento import Equipamento
from seguranca_trabalho.submodels.enums import TipoEquipamento

TIPO_EQUIPAMENTO_OPTIONS = (
    (TipoEquipamento.NONE, "..."),
    (TipoEquipamento.EPI, "EPI"),
    (TipoEquipamento.EPC, "EPC"),
)
class EquipamentoForm(forms.ModelForm):
    tipo = forms.ChoiceField(widget=forms.Select, choices=TIPO_EQUIPAMENTO_OPTIONS)
    prazo_validade = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" }), required=False)
    class Meta:
        model = Equipamento
        fields = ["codigo",
            "descricao",
            "tipo",
            "hierarquia_protecao_coletiva",
            "prazo_validade",
            "certificado_aprovacao",
            "url_foto",
            "comentario"]
