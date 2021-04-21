from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from seguranca_trabalho._forms.equipamento import EquipamentoForm

@login_required(login_url="login")
def criar_equipamento(request):
    success = False
    msg = None
    form = EquipamentoForm()
    if request.POST:
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            success = True
            msg = "Equipamento criado com sucesso"
            form.save()
    return render(request, "seguranca_trabalho/cadastros/formulario_epi.html", { "form": form, "msg" : msg, "success" : success })