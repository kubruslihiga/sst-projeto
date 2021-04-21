# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.forms.models import model_to_dict
from seguranca_trabalho.submodels.usuario import Usuario
from seguranca_trabalho.submodels.empresa import Empresa

@login_required(login_url="/login/")
def index(request:HttpRequest):    
    context = {}
    context['segment'] = 'index'
    usuario: Usuario = request.user
    if usuario.empresas.exists():
        if usuario.empresa_selecionada is None:
           primeira_empresa = usuario.empresas.all()[0]
           usuario.empresa_selecionada = primeira_empresa
           usuario.save()
        empresas = []
        [empresas.append(model_to_dict(e)) for e in usuario.empresas.all()]
        request.session['empresas'] = empresas
    else:
        return redirect("/logout?msg=O usuário não possui empresa em seu cadastro. Favor contactar o administrador do sistema.")
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def empresa(request:HttpRequest):
    if request.POST:
        post = request.POST
        empresa_id = post['empresa']
        if empresa_id:
            print(empresa_id)
            empresa = Empresa.objects.filter(id=empresa_id).get()
            usuario:Usuario = request.user
            usuario.empresa_selecionada = empresa
            usuario.save()
    context = {}
    context['segment'] = 'index'
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
