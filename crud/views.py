import csv
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from .forms import UsuarioForm
from .models import Usuario


import json


def cadastrar(request):
    form = UsuarioForm(request.POST or None)
    usuario = Usuario.objects.all()

    if form.is_valid():
        form.save()

    return render(request, 'cadastrar.html', {'form': form})


def detalhes(request):
    usuario = Usuario.objects.all()
    return render(request, 'detalhes.html', {'usuario': usuario})


def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST, instance=usuario)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'editar.html', {'usuario': usuario})


def deletar(request, id):
    form = Usuario.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')


def json(request):
    data = list(Usuario.objects.values())
    return JsonResponse({'data': data})


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="usuarios.csv"'
    writer = csv.writer(response)
    writer.writerow(['Usuario', 'Senha', 'Data Nascimento'])

    usuarios = Usuario.objects.all().values_list('id_usuario', 'senha', 'dataNascimento')
    for usuario in usuarios:
        writer.writerow(usuario)

    return response








