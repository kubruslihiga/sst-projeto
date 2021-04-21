from django import forms

from seguranca_trabalho.submodels.equipamento import Equipamento

class EquipamentoForm(forms.ModelForm):
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
