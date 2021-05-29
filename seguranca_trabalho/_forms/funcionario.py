import re
from django.core.validators import EMPTY_VALUES
from seguranca_trabalho.submodels.enums import Genero
from django import forms
from django.forms import ValidationError

from seguranca_trabalho.submodels.funcionario import Funcionario
from seguranca_trabalho.submodels.enums import Genero


cpf_error_messages = {
    'invalid': "Número do CPF inválido.",
    'digits_only': "O campo aceita apenas dígitos numéricos.",
    'max_digits': "O CPF deve ter 11 dígitos numéricos.",
}

GENERO_OPTIONS = (
    (Genero.NONE, "..."),
    (Genero.FEMALE, "Feminino"),
    (Genero.MALE, "Masculino"),
)

def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0

def cpf_validator(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(cpf_error_messages['digits_only'])
    if len(value) != 11:
        raise ValidationError(cpf_error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(cpf_error_messages['invalid'])
    return orig_value

class FuncionarioForm(forms.ModelForm):
    data_exame_admissional = forms.DateField(
        input_formats=['%d/%m/%Y'],
        error_messages={ "invalid": "O formato da data deve ser dd/mm/yyyy"},
        widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999", "class": "input-datepicker" } ))
    data_exame_demissional = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        error_messages={ "invalid": "O formato da data deve ser dd/mm/yyyy"},
        widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999", "class": "input-datepicker" }), required=False)
    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        error_messages={ "invalid": "O formato da data deve ser dd/mm/yyyy"},
        widget=forms.DateInput(format="%d/%m/%Y", attrs={ "data-mask": "99/99/9999", "class": "input-datepicker" }), required=True)
    cpf = forms.CharField(
        required=True,
        max_length=14,
        validators=[cpf_validator],
        widget=forms.TextInput(attrs={ "data-mask": "000.000.000-00", "data-mask-reverse": "true" }))
    genero = forms.ChoiceField(choices = GENERO_OPTIONS, required=True)
    class Meta:
        model = Funcionario
        fields = ["estagiario",
                  "codigo_erp",
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
                  "data_exame_admissional",
                  "data_exame_demissional",
                  "setor",
                  "cargo",
                  "funcao",
                  "url_imagem"]
