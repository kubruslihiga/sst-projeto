from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from seguranca_trabalho._forms.equipamento import EquipamentoForm
from seguranca_trabalho.submodels.usuario import Usuario
from seguranca_trabalho.submodels.equipamento import Equipamento

_link = "/epi"
@login_required(login_url="login")
def criar_equipamento(request):
    success = False
    msg = None
    form = EquipamentoForm()
    if request.POST:
        usuario:Usuario = request.user
        form = EquipamentoForm(request.POST, initial={'empresa': usuario.empresa_selecionada})
        if form.is_valid():
            success = True
            msg = "Equipamento criado com sucesso"
            equipamento = form.save(commit=False)
            equipamento.empresa = usuario.empresa_selecionada
            equipamento.save()
            return recuperar_equipamentos(request)
        else:
            print(form.errors)
    return render(request, "seguranca_trabalho/cadastros/formulario_epi.html", { "form": form, "msg" : msg, "success" : success, "link": _link })

@login_required(login_url="login")
def recuperar_equipamentos(request):
    usuario:Usuario = request.user
    if usuario.empresa_selecionada:
        equipamentos = Equipamento.objects.filter(empresa=usuario.empresa_selecionada)
    return render(request, "seguranca_trabalho/cadastros/listas_equipamento.html", { "equipamentos": equipamentos })

@login_required(login_url="login")
def detalhar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    usuario:Usuario = request.user
    if equipamento.empresa != request.user.empresa_selecionada:
        return render(request, "seguranca_trabalho/cadastros/listas_equipamento.html", { "equipamento": equipamento })
    form = EquipamentoForm(instance=equipamento)
    success = False
    msg = ""
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            success = True
            msg = "Equipamento criado com sucesso"
            equipamento = form.save(commit=False)
            equipamento.empresa = usuario.empresa_selecionada
            equipamento.save()
            return recuperar_equipamentos(request)
    return render(request, "seguranca_trabalho/cadastros/formulario_epi.html", { "form": form, "msg" : msg, "success" : success, "link": _link })