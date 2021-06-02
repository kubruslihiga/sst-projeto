from django.http.response import Http404, HttpResponse
from seguranca_trabalho.submodels.usuario import Usuario
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from seguranca_trabalho._forms.funcionario_epi import FuncionarioEPIForm
from seguranca_trabalho.submodels.equipamento import Equipamento, FuncionarioEquipamento
from seguranca_trabalho._views.funcionario import recuperar_funcionarios
from seguranca_trabalho._views.equipamento import recuperar_equipamentos
from seguranca_trabalho.submodels.funcionario import Funcionario

_link = "/funcionario_epi"

@login_required(login_url="login")
def recuperar_funcionario_epis(request):
    usuario:Usuario = request.user
    if usuario.empresa_selecionada:
        funcionario_epi_list = FuncionarioEquipamento.objects.filter(empresa=usuario.empresa_selecionada).order_by('funcionario__nome')
    return render(request, "seguranca_trabalho/cadastros/listas_funcionario_epi.html", { "funcionario_epis": funcionario_epi_list })

@login_required(login_url="login")
def detalhar_funcionario_epi(request, id):
    try:
        funcionario_epi = get_object_or_404(FuncionarioEquipamento, pk=id)
        usuario:Usuario = request.user
        if funcionario_epi.empresa != request.user.empresa_selecionada:
            request.alert_warning_message = "Associação funcionário e equipamento não é da empresa selecionada."
            return recuperar_funcionario_epis(request)
        form = FuncionarioEPIForm(instance=funcionario_epi)
        success = False
        msg = ""
        if request.method == 'POST':
            form = FuncionarioEPIForm(request.POST, instance=funcionario_epi)
            if form.is_valid():
                success = True
                msg = "Associação funcionário e equipamento foi alterada com sucesso."
                funcionario = form.save(commit=False)
                funcionario.empresa = usuario.empresa_selecionada
                funcionario.save()
                request.alert_success_message = msg
                return recuperar_funcionario_epis(request)
        return render(request, "seguranca_trabalho/cadastros/formulario_funcionario.html", { "form": form, "msg" : msg, "success" : success, "link": _link })
    except Http404:
        request.alert_warning_message = "Identificador do funcionário/equipamento não está permitido para alteração."
        resp:HttpResponse = recuperar_funcionario_epis(request)
        return resp

@login_required(login_url="login")
def associar_equipamento(request, id):
    try:
        funcionario = get_object_or_404(Funcionario, pk=id)
        usuario:Usuario = request.user
        if funcionario.empresa != usuario.empresa_selecionada:
            request.alert_warning_message = "O funcionário não está associada a empresa selecionada."
            return recuperar_funcionarios(request)
        if request.method == 'POST':
            POST = request.POST.copy()
            POST['funcionario'] = funcionario
            form = FuncionarioEPIForm(usuario, POST)
            if form.is_valid():
                msg = "Associação funcionário e equipamento criada com sucesso"
                f = form.save(commit=False)
                f.empresa = usuario.empresa_selecionada
                f.save()
                request.alert_success_message = msg
                return recuperar_funcionarios(request)
        else:
            form = FuncionarioEPIForm(usuario, initial={'funcionario': funcionario}, disabled_fields=["funcionario"])
        return render(request, "seguranca_trabalho/cadastros/formulario_funcionario_epi.html", { "form": form, "msg" : "", "success" : "" })
    except Http404:
        request.alert_warning_message = "O funcionário não existe."
        resp:HttpResponse = recuperar_funcionarios(request)
        return resp

@login_required(login_url="login")
def associar_funcionario(request, id):
    try:
        equipamento = get_object_or_404(Equipamento, pk=id)
        usuario:Usuario = request.user
        if equipamento.empresa != usuario.empresa_selecionada:
            request.alert_warning_message = "O equipamento não está associada a empresa selecionada."
            return recuperar_equipamentos(request, equipamento)

        if request.method == 'POST':
            POST = request.POST.copy()
            POST['equipamento'] = equipamento
            form = FuncionarioEPIForm(usuario, POST)
            if form.is_valid():
                msg = "Associação funcionário e equipamento criada com sucesso"
                f = form.save(commit=False)
                f.empresa = usuario.empresa_selecionada
                f.save()
                request.alert_success_message = msg
                return recuperar_equipamentos(request)
        else:
            form = FuncionarioEPIForm(usuario, initial={'equipamento': equipamento}, disabled_fields=["equipamento"])
        return render(request, "seguranca_trabalho/cadastros/formulario_funcionario_epi.html", { "form": form, "msg" : "", "success" : "" })
    except Http404:
        request.alert_warning_message = "O equipamento não existe."
        resp:HttpResponse = recuperar_equipamentos(request)
        return resp