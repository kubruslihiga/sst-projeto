from django import forms

from seguranca_trabalho.submodels.equipamento import FuncionarioEquipamento
from seguranca_trabalho.submodels.usuario import Usuario

class FuncionarioEPIForm(forms.ModelForm):
    funcionarios = forms.ModelChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple, label="Funcionários", to_field_name="nome")

    def __init__(self, user:Usuario, *args, **kwargs):
        super(FuncionarioEPIForm, self).__init__(*args, **kwargs)
        self.fields['funcionarios'].queryset=FuncionarioEquipamento.objects.filter(empresa=user.empresa_selecionada)

    class Meta:
        model = FuncionarioEquipamento
        fields = ["funcionarios", "equipamento",
                    "quantidade",
                    "data_entrega",
                    "devolucao",
                    "data_devolucao",
                    "data_vencimento",
                    "comentario"]