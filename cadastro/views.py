from django.shortcuts import render

def primeira_pagina(request):
    return render(request, 'cadastro/pagina.html')

def entrar_site(request):
    return render(request, 'cadastro/tela_inicial.html')

