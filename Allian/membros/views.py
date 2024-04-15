from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MembroForm
from .models import Membro
from datetime import datetime, date, timedelta
from django.db.models import Q
from django.http import JsonResponse

@login_required
def lista_membros(request):
    search = request.GET.get('search')
    data = request.GET.get('data')

    if search:
        membros = Membro.objects.filter(nome__icontains=search, user=request.user)
    elif data:
        data_date = datetime.strptime(data, "%Y-%m-%d").date()
        membros = Membro.objects.filter(data_aniversario__day=data_date.day, data_aniversario__month=data_date.month, user=request.user)
    else:
        membros_list = Membro.objects.all().order_by('nome').filter(user=request.user)

        paginator = Paginator(membros_list, 10)

        page = request.GET.get('page')

        membros = paginator.get_page(page)
    return render(request, 'membros/lista_membros.html', {'membros': membros})

@login_required
def lista_membros_ajax(request):
    search = request.GET.get('search')
    data = request.GET.get('data')

    if search:
        membros = Membro.objects.filter(nome__icontains=search, user=request.user)
    elif data:
        data_date = date.fromisoformat(data)  # Python 3.7+ syntax to parse ISO date
        membros = Membro.objects.filter(data_aniversario=data_date, user=request.user)
    else:
        membros = Membro.objects.select_related('empresa_cliente').filter(user=request.user)

    membros_data = [{'id': membro.id, 'nome': membro.nome, 'nome_empresa': membro.empresa_cliente.nome} for membro in membros]

    # Busca por aniversários de membros hoje até daqui a 7 dias
    hoje = date.today()
    aniversarios_proximos = Membro.objects.filter(
        data_aniversario__range=[hoje, hoje + timedelta(days=7)],
        user=request.user
    ).values('nome', 'data_aniversario')

    notificacoes_aniversarios = []

    for membro in aniversarios_proximos:
        notificacoes_aniversarios.append({
            'nome': membro['nome'],
            'tipo': 'Aniversário',
            'data': membro['data_aniversario']
        })

    return JsonResponse({'notificacoes_aniversarios': notificacoes_aniversarios, 'membros': membros_data})

@login_required
def adicionar_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST)

        if form.is_valid():
            membro = form.save(commit=False)
            membro.user = request.user
            membro.save()

            messages.success(request, 'Membro adicionado com sucesso!')

            return redirect('/membros/lista/')
    else:
        form = MembroForm()
    return render(request, 'membros/adicionar_membro.html', {'form': form})

@login_required
def atualizar_membro(request, id):
    membro = get_object_or_404(Membro, pk=id)
    form = MembroForm(instance=membro)

    if(request.method == 'POST'):
        form = MembroForm(request.POST, instance=membro)

        if(form.is_valid()):
            membro.save()

            messages.success(request, 'Membro atualizado com sucesso!')

            return redirect('/membros/lista/')
        else:
            return render(request, 'membros/atualizar_membro.html', {'form': form, 'membro': membro})

    else:
        return render(request, 'membros/atualizar_membro.html', {'form': form, 'membro': membro})

@login_required
def deletar_membro(request, id):
    membro = get_object_or_404(Membro, pk=id)
    membro.delete()

    messages.success(request, 'Membro deletado com sucesso!')
    return redirect('/membros/lista/')

