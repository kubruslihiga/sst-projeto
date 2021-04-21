from django.shortcuts import render
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from seguranca_trabalho.forms import ComunicacaoAcidenteTrabalhoForm, MonitoramentoSaudeTrabalhadorForm

@login_required(login_url='login')
# @admin_only
def criar_cat(request):
    success = False
    msg = None
    form = ComunicacaoAcidenteTrabalhoForm()
    if request.POST:
        form = ComunicacaoAcidenteTrabalhoForm(request.POST)
        if form.is_valid():
            success = True
            msg = "CAT criada com sucesso"
            form.save()
    return render(request, "seguranca_trabalho/comunicacao_acidente_trabalho/formulario_cat.html", { "form": form, "msg" : msg, "success" : success })

def criar_monitoramento_trabalhador(request):
    success = False
    msg = None
    form = MonitoramentoSaudeTrabalhadorForm()
    if request.POST:
        form = MonitoramentoSaudeTrabalhadorForm(request.POST)
        if form.is_valid():
            success = True
            msg = "Monitoramento saúde do trabalhador criada com sucesso"
            form.save()
    return render(request, "seguranca_trabalho/monitoramento_saude_trabalhador/formulario_monitoramento.html", { "form": form, "msg" : msg, "success" : success })

def criar_condicao_fator_risco(request):
    success = False
    msg = None
    form = MonitoramentoSaudeTrabalhadorForm()
    if request.POST:
        form = MonitoramentoSaudeTrabalhadorForm(request.POST)
        if form.is_valid():
            success = True
            msg = "Monitoramento saúde do trabalhador criada com sucesso"
            form.save()
    return render(request, "seguranca_trabalho/condicao_fator_risco_ambiente_trabalho/formulario_condicao_risco.html", { "form": form, "msg" : msg, "success" : success })
