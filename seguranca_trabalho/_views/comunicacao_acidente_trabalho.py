from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from seguranca_trabalho._forms.comunicacao_acidente_trabalho import ComunicacaoAcidenteTrabalhoForm

@login_required(login_url='login')
def criar_comunicacao_acidente_trabalho(request):
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