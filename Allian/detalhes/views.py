from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ComputadorForm
from .models import Computador
from empresas.models import Empresa

@login_required
def ListaComputadores(request, id):
    empresa = Empresa.objects.get(pk=id)
    search = request.GET.get('search')

    if search:
        empresa.nome = search
        computadores = Computador.objects.filter(empresa__nome__icontains=empresa.nome, user=request.user)
    else:
        computadores_list = Computador.objects.filter(empresa=empresa, user=request.user).order_by('empresa')

        paginator = Paginator(computadores_list, 10)

        page = request.GET.get('page')

        computadores = paginator.get_page(page)
    return render(request, 'empresas/detalhes/lista_computadores.html', {'computadores': computadores, 'empresa': empresa})

@login_required
def AdicionarComputador(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if request.method == 'POST':
        form = ComputadorForm(request.POST)

        if form.is_valid():
            computador = form.save(commit=False)
            computador.user = request.user
            computador.empresa = Empresa.objects.get(pk=id)
            computador.save()

            messages.success(request, 'Computador adicionado com sucesso!')

            return redirect('lista-computadores', empresa.id)

    else:
        form = ComputadorForm()
        return render(request, 'empresas/detalhes/adicionar_computador.html', {'form': form, 'empresa': empresa})

@login_required
def AtualizarComputador(request, id, pk):
    empresa = get_object_or_404(Empresa, pk=id)
    computador = get_object_or_404(Computador, pk=pk)
    form = ComputadorForm(instance=computador)

    if(request.method == 'POST'):
        form = ComputadorForm(request.POST, instance=computador)

        if form.is_valid():
            computador.save()

            messages.success(request, 'Computador atualizado com sucesso!')

            return redirect('lista-computadores', empresa.id)
        else:
            return render(request, 'empresas/detalhes/atualizar_computador.html', {'form': form, 'computador': computador, 'empresa': empresa})

    else:
        return render(request, 'empresas/detalhes/atualizar_computador.html', {'form': form, 'computador': computador, 'empresa': empresa})

@login_required
def DeletarComputador(request, id, pk):
    empresa = get_object_or_404(Empresa, pk=id)
    computador = get_object_or_404(Computador, pk=pk)
    computador.delete()

    messages.success(request, 'Computador deletado com sucesso!')
    return redirect('lista-computadores', empresa.id)

