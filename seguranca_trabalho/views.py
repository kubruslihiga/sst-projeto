from django.shortcuts import render
from .decorators import unauthenticated_user, allowed_users, admin_only
from seguranca_trabalho.forms import MonitoramentoSaudeTrabalhadorForm

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
