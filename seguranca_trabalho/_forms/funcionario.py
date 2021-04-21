from django import forms

from seguranca_trabalho.submodels.funcionario import Funcionario

class FuncionarioForm(forms.ModelForm):
    data_exame_admissional = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" } ))
    data_exame_demissional = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" }), required=False)
    data_nascimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999" }), required=True)
    class Meta:
        model = Funcionario
        fields = ["codigo_erp",
                    "codigo_esocial",
                    "nome",
                    "genero",
                    "cbo",
                    "cpf",
                    "rg",
                    "nis",
                    "pis",
                    "pasep",
                    "nit",
                    "data_nascimento",
                    "estagiario",
                    "data_exame_admissional",
                    "data_exame_demissional",
                    "setor",
                    "cargo",
                    "funcao",
                    "url_imagem"]