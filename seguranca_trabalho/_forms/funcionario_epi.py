from seguranca_trabalho.submodels.funcionario import Funcionario
from django import forms
from django.forms import ValidationError

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
    comentario = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={ "rows": "3", "class": "textarea" }))

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

    def clean(self):
        if self.cleaned_data['data_vencimento'] <= self.cleaned_data['data_entrega']:
            raise ValidationError("A data de vencimento do equipamento deve ser posterior a data de entrega")
            

    class Meta:
        model = FuncionarioEquipamento
        fields = ["funcionario", "equipamento",
                    "quantidade",
                    "data_entrega",
                    "devolucao",
                    "data_devolucao",
                    "data_vencimento",
                    "comentario"]