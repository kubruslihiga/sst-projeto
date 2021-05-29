import re
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from seguranca_trabalho._forms.funcionario import FuncionarioForm
from seguranca_trabalho.submodels.usuario import Usuario
from seguranca_trabalho.submodels.funcionario import Funcionario

_link = "/funcionario"
@login_required(login_url="login")
def criar_funcionario(request):
    success = False
    msg = None
    form = FuncionarioForm()
    if request.POST:
        usuario:Usuario = request.user
        POST = request.POST.copy()
        POST.update({'cpf': re.sub("[^0-9]", "", POST.cpf)})
        form = FuncionarioForm(POST, initial={'empresa': usuario.empresa_selecionada})
        if form.is_valid():
            success = True
            msg = "Funcionário criado com sucesso"
            funcionario = form.save(commit=False)
            funcionario.empresa = usuario.empresa_selecionada
            funcionario.save()
            request.alert_success_message = "Funcionário criado com sucesso."
            return recuperar_funcionarios(request)
        else:
            print(form.errors)
    return render(request, "seguranca_trabalho/cadastros/formulario_funcionario.html", { "form": form, "msg" : msg, "success" : success, "link": _link })

@login_required(login_url="login")
def recuperar_funcionarios(request):
    usuario:Usuario = request.user
    funcionarios = []
    if usuario.empresa_selecionada:
        funcionarios = Funcionario.objects.filter(empresa=usuario.empresa_selecionada)
    return render(request, "seguranca_trabalho/cadastros/listas_funcionario.html", { "funcionarios": funcionarios })

@login_required(login_url="login")
def detalhar_funcionario(request, id):
    try:
        funcionario = get_object_or_404(Funcionario, pk=id)
        usuario:Usuario = request.user
        if funcionario.empresa != request.user.empresa_selecionada:
            request.alert_warning_message = "Funcionário não está associado a empresa."
            return recuperar_funcionarios(request)
        form = FuncionarioForm(instance=funcionario)
        success = False
        msg = ""
        if request.method == 'POST':
            POST = request.POST.copy()
            POST.update({'cpf': re.sub("[^0-9]", "", POST['cpf'])})
            form = FuncionarioForm(POST, instance=funcionario)
            if form.is_valid():
                success = True
                msg = "Funcionário criado com sucesso"
                funcionario = form.save(commit=False)
                funcionario.empresa = usuario.empresa_selecionada
                funcionario.save()
                request.alert_success_message = "Funcionário alterado com sucesso."
                return recuperar_funcionarios(request)
        return render(request, "seguranca_trabalho/cadastros/formulario_funcionario.html", { "form": form, "msg" : msg, "success" : success, "link": _link })
    except Http404:
        request.alert_warning_message = "Identificador do funcionário não está permitido para alteração."
        resp:HttpResponse = recuperar_funcionarios(request)
        return resp
        