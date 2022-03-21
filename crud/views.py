from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UsuarioForm
from .models import Usuario




def cadastrar(request, password=None):
    form = UsuarioForm(request.POST or None)
    usuario = Usuario.objects.all()
    if form.is_valid():
        form.save()

    return render(request,'cadastrar.html',{'form':form})



def detalhes(request):
    usuario = Usuario.objects.all()
    return render(request,'detalhes.html',{'usuario':usuario})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST, instance=usuario)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'editar.html',{'usuario':usuario})

def deletar(request, id):
    form = Usuario.objects.get(id=id)
    form.delete()
    return  HttpResponseRedirect('/')




