from seguranca_trabalho.submodels.funcionario import Funcionario
from django import forms

from seguranca_trabalho.submodels.equipamento import Equipamento, FuncionarioEquipamento
from seguranca_trabalho.submodels.funcionario import Funcionario

class FuncionarioEPIForm(forms.ModelForm):
    #funcionarios = forms.ModelChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple, label="Funcionários", to_field_name="nome")
    data_entrega = forms.DateField(
        input_formats=['%d/%m/%Y'],
        error_messages={ "invalid": "O formato da data deve ser dd/mm/yyyy"},
        widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" }), 
        required= True)
    data_devolucao = forms.DateField(
        input_formats=['%d/%m/%Y'],
        error_messages={ "invalid": "O formato da data deve ser dd/mm/yyyy"},
        widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" }), 
        required=False )
    data_vencimento = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        error_messages={ "invalid": "O formato da data deve ser dd/mm/yyyy"},
        widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" } ))
    def __init__(self, usuario, *args, **kwargs):
        disabled_fields = []
        if kwargs.get("disabled_fields") is not None:
            disabled_fields = kwargs["disabled_fields"]
            del kwargs["disabled_fields"]
        super(FuncionarioEPIForm, self).__init__(*args, **kwargs)
        for d_field in disabled_fields:
            self.fields[d_field].disabled = True
        self.fields['funcionario'].queryset=Funcionario.objects.filter(empresa=usuario.empresa_selecionada)
        self.fields['equipamento'].queryset=Equipamento.objects.filter(empresa=usuario.empresa_selecionada)

    class Meta:
        model = FuncionarioEquipamento
        fields = ["funcionario", "equipamento",
                    "quantidade",
                    "data_entrega",
                    "devolucao",
                    "data_devolucao",
                    "data_vencimento",
                    "comentario"]