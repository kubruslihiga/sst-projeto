from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from seguranca_trabalho._forms.funcionario_epi import FuncionarioEPIForm
from seguranca_trabalho.submodels.equipamento import FuncionarioEquipamento

_link = "/funcionario_epi"
@login_required(login_url="login")
def criar_funcionario_epi(request):
    success = False
    msg = None
    usuario:Usuario = request.user
    form = FuncionarioEPIForm(usuario)
    if request.POST:
        form = FuncionarioEPIForm(usuario, request.POST)
        if form.is_valid():
            success = True
            msg = "Associação funcionário e equipamento criada com sucesso"
            f = form.save(commit=False)
            f.empresa = usuario.empresa_selecionada
            f.save()
    return render(request, "seguranca_trabalho/cadastros/formulario_funcionario_epi.html", { "form": form, "msg" : msg, "success" : success })

@login_required(login_url="login")
def recuperar_funcionario_epis(request):
    usuario:Usuario = request.user
    if usuario.empresa_selecionada:
        funcionario_epi_list = FuncionarioEquipamento.objects.filter(empresa=usuario.empresa_selecionada)
    return render(request, "seguranca_trabalho/cadastros/listas_funcionario_epi.html", { "funcionario_epis": funcionario_epi_list })

@login_required(login_url="login")
def detalhar_funcionario_epi(request, id):
    funcionario_epi = get_object_or_404(FuncionarioEquipamento, pk=id)
    usuario:Usuario = request.user
    if funcionario.empresa != request.user.empresa_selecionada:
        return render(request, "seguranca_trabalho/cadastros/listas_funcionario_epi.html", { "funcionario_epis": funcionario_epi_list })
    form = FuncionarioForm(instance=funcionario)
    success = False
    msg = ""
    if request.method == 'POST':
        form = FuncionarioEPIForm(usuario, request.POST, instance=funcionario)
        if form.is_valid():
            success = True
            msg = "Funcionário/EPI criado com sucesso"
            funcionario = form.save(commit=False)
            funcionario.empresa = usuario.empresa_selecionada
            funcionario.save()
    return render(request, "seguranca_trabalho/cadastros/formulario_funcionario.html", { "form": form, "msg" : msg, "success" : success, "link": _link })