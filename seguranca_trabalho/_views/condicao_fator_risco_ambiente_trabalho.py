from django.http.request import HttpRequest
from seguranca_trabalho.submodels.condicao_fator_risco_ambiente_trabalho import CondicaoAmbientalFatorRisco, CondicaoFator
from django.forms.models import inlineformset_factory, modelformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from seguranca_trabalho._forms.condicao_fator_risco_ambiente_trabalho import AnaliseEPIFormset, CondicaoFatorFormset, CondicaoAmbientalFatorRiscoForm

@login_required(login_url='login')
def criar_condicao_fator_risco_ambiente_trabalho(request):
    form = CondicaoAmbientalFatorRiscoForm(request.user)
    condicao_fator_formset = CondicaoFatorFormset()
    context = { "form": form, "condicao_fator_formset": condicao_fator_formset }
    if request.POST:
        form = CondicaoAmbientalFatorRiscoForm(request.user, request.POST)
        if form.is_valid():
            condicao_ambiental_fator_risco:CondicaoAmbientalFatorRisco = form.save(commit=False)
            condicao_ambiental_fator_risco.empresa = request.user.empresa_selecionada
            condicao_ambiental_fator_risco.save()
            return redirect(f"/condicao_fator_risco_ambiente_trabalho/{condicao_ambiental_fator_risco.pk}/fator_risco")
        else:
            print(form.errors)
    return render(request, "seguranca_trabalho/condicao_ambiente_fator_risco/formulario_condicao_ambiente_fator_risco.html", context)

@login_required(login_url='login')
def configurar_fator_risco(request:HttpRequest, id):
    pass