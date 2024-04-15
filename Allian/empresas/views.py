from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import EmpresaForm
from .models import Empresa
from tarefas.models import Tarefa
from membros.models import Membro
from django.http import JsonResponse

@login_required
def dashboard(request):

    # Obtenha a data atual
    data_atual = date.today()

    # Filtrar tarefas com data igual à data atual
    tarefas = Tarefa.objects.filter(data_realizacao__date=data_atual)

    # Filtrar clientes com aniversário igual à data atual
    membros = Membro.objects.filter(data_aniversario__month=data_atual.month, data_aniversario__day=data_atual.day)



    # Passe os dados filtrados para o template
    return render(request, 'dashboard.html', {'tarefas': tarefas, 'membros': membros, 'data_atual': data_atual})

@login_required
def lista_empresas(request):
    search = request.GET.get('search')

    numSistema = request.GET.get('numSistema')

    if search:
        empresas = Empresa.objects.filter(nome__icontains=search, user=request.user)
    elif numSistema:
        empresas = Empresa.objects.filter(id_sistema__icontains=numSistema, user=request.user)
    else:
        empresas_list = Empresa.objects.all().order_by('nome').filter(user=request.user)

        paginator = Paginator(empresas_list, 10)

        page = request.GET.get('page')

        empresas = paginator.get_page(page)

    return render(request, 'empresas/lista_empresas.html', {'empresas': empresas})

@login_required
def lista_empresas_ajax(request):
    search = request.GET.get('search')
    numSistema = request.GET.get('numSistema')

    if search:
        empresas = Empresa.objects.filter(nome__icontains=search, user=request.user)
    elif numSistema:
        empresas = Empresa.objects.filter(id_sistema__icontains=numSistema, user=request.user)
    else:
        empresas = Empresa.objects.all().order_by('nome').filter(user=request.user)

    # Verificar certificados vencidos ou próximos a vencer
    hoje = date.today()
    sete_dias = hoje + timedelta(days=7)
    certificados_para_notificar = []

    for empresa in empresas:
        if empresa.data_certificado:
            try:
                # Converter a string 'data_certificado' em um objeto datetime.date
                data_certificado = datetime.strptime(empresa.data_certificado, '%d/%m/%Y').date()
                if data_certificado <= sete_dias:
                    certificados_para_notificar.append({
                        'empresa_id': empresa.id,
                        'nome': empresa.nome,
                        'data_certificado': data_certificado.strftime('%Y-%m-%d')
                    })
            except ValueError:
                # Tratar o caso em que a conversão falha (data inválida)
                print(f"Erro ao converter data_certificado para empresa ID {empresa.id}")

    # Aqui, em vez de renderizar um template, retornamos JSON com as empresas e notificações
    empresas_data = [{'id': empresa.id, 'nome': empresa.nome, 'id_sistema': empresa.id_sistema} for empresa in empresas]

    return JsonResponse({'empresas': empresas_data, 'notificacoes': certificados_para_notificar})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

@login_required
def adicionar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.user = request.user
            empresa.save()

            messages.success(request, 'Empresa adicionada com sucesso!')

            return redirect('/empresas/lista')

    else:
        form = EmpresaForm()
        return render(request, 'empresas/adicionar_empresa.html', {'form': form})

@login_required
def atualizar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = EmpresaForm(instance=empresa)

    if(request.method == 'POST'):
        form = EmpresaForm(request.POST, instance=empresa)

        if form.is_valid():
            empresa.save()

            messages.success(request, 'Empresa atualizada com sucesso!')

            return redirect('/empresas/lista/')
        else:
            return render(request, 'empresas/atualizar_empresa.html', {'form': form, 'empresa': empresa})

    else:
        return render(request, 'empresas/atualizar_empresa.html', {'form': form, 'empresa': empresa})

@login_required
def deletar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    empresa.delete()

    messages.success(request, 'Empresa deletada com sucesso!')
    return redirect('/empresas/lista/')
