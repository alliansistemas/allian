from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date, datetime

from .forms import TarefaForm
from .models import Tarefa

from membros.models import Membro

from django.db.models import Q

@login_required
def lista_tarefas(request):
    today = date.today()

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    data = request.GET.get('data')

    if search:
        tarefas = Tarefa.objects.filter(Q(atividade__icontains=search) | Q(atividade__icontains=search.lower()) | Q(atividade__icontains=search.upper()), user=request.user)
    elif data:
        tarefas = Tarefa.objects.filter(data_realizacao__date=data, user=request.user)
    elif (filter == 'resolvida' or filter == 'pendente'):
        tarefas = Tarefa.objects.filter(finalizada=filter, data_realizacao__date=today, user=request.user).order_by('data_realizacao')
    elif (filter == 'todas'):
        tarefas = Tarefa.objects.all()
    else:
        tarefas_list = Tarefa.objects.filter(user=request.user, data_realizacao__date=today).order_by('data_realizacao')

        paginator = Paginator(tarefas_list, 10)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)

        for tarefa in tarefas:
            tarefa.membro = Membro.objects.filter(id=tarefa.nome_cliente_id).first()

    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

@login_required
def adicionar_tarefas(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.finalizada = 'pendente'
            tarefa.user = request.user
            tarefa.save()

            messages.success(request, 'Tarefa adicionada com sucesso!')

            return redirect('/tarefas/lista/')
    else:
        form = TarefaForm()
    membros = Membro.objects.all()
    return render(request, 'tarefas/adicionar_tarefa.html', {'form':form, 'membros': membros})

@login_required
def atualizar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    form = TarefaForm(instance=tarefa)

    if(request.method == 'POST'):
        form = TarefaForm(request.POST, instance=tarefa)

        if(form.is_valid()):
            agora = datetime.now()
            tarefa.data_realizacao = agora
            tarefa.save()

            messages.success(request, 'Tarefa atualizada com sucesso!')

            return redirect('/tarefas/lista/')
        else:
            return render(request, 'tarefas/atualizar_tarefa.html',
                {'form': form, 'tarefa': tarefa})

    else:
        return render(request, 'tarefas/atualizar_tarefa.html',
            {'form': form, 'tarefa': tarefa})

@login_required
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()

    messages.success(request, 'Tarefa deletada com sucesso!')
    return redirect('/tarefas/lista/')

@login_required
def alterar_status(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)



    if(tarefa.finalizada == 'pendente'):
        tarefa.finalizada = 'resolvida'

        messages.success(request, 'Tarefa alterada para "Concluída"!')
    else:
        tarefa.finalizada = 'pendente'

        messages.warning(request, 'Tarefa alterada para "Pendente"!')

    agora = datetime.now()
    tarefa.data_realizacao = agora
    tarefa.save()

    return redirect('/tarefas/lista/')
