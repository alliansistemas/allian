from datetime import date
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from .models import Empresa, Membro, Tarefa


def home(request):
    return render(request, 'home.html')


def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.first_name = nome
            user.save()

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Houve algum erro, realize login manualmente!')
        else:
            messages.error(request, 'Nome de usuário já existente!')

    return render(request, 'cadastro_usuario.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bem vindo, {user.first_name}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário/senha incorretos!')

    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def cadastro_empresa(request):
    if request.method == 'POST':
        id_sistema = request.POST.get('id_sistema')
        nome = request.POST.get('nome_empresa')
        admin = request.POST.get('nome_administrador')

        if id_sistema and nome and admin:
            empresas = Empresa(id_sistema=id_sistema, nome=nome, administrador=admin)
            empresas.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('empresas')

    return render(request, 'cadastro_empresa.html')


def atualizar_empresa(request, pk):
    empresa = Empresa.objects.get(id=pk)

    if request.method == 'POST':
        id_sistema = request.POST.get('id_sistema')
        nome = request.POST.get('nome_empresa')
        admin = request.POST.get('nome_administrador')

        if id_sistema and nome and admin:
            empresa.id_sistema = id_sistema
            empresa.nome = nome
            empresa.administrador = admin
            empresa.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('empresas')

    return render(request, 'atualizar_empresa.html', {'empresa': empresa})


def deletar_empresa(request, pk):
    empresa = Empresa.objects.get(id=pk)
    if request.method == 'POST':
        empresa.delete()
        messages.success('Empresa deletada com sucesso!')
        return redirect('empresas')

    return render(request, 'deletar_empresa.html', {'empresa': empresa})


def empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas})


def cadastro_cliente(request):
    if request.method == 'POST':
        empresa_cliente = request.POST.get('id_empresa')
        nome = request.POST.get('id_nome')
        data_aniversario = request.POST.get('id_aniversario')

        if empresa_cliente and nome and data_aniversario:
            empresas = Empresa.objects.get(pk=empresa_cliente)
            clientes = Membro(empresa_cliente=empresas, nome=nome, data_aniversario=data_aniversario)
            clientes.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('clientes')

    empresas = Empresa.objects.all()
    return render(request, 'cadastro_cliente.html', {'empresas': empresas})


def atualizar_cliente(request, pk):
    cliente = Membro.objects.get(id=pk)

    if request.method == 'POST':
        nome = request.POST.get('id_nome')
        data_aniversario = request.POST.get('id_aniversario')
        empresa_cliente = request.POST.get('id_empresa')

        if nome and data_aniversario and empresa_cliente:
            cliente.empresa_cliente = empresa_cliente
            cliente.nome = nome
            cliente.data_aniversario = data_aniversario
            cliente.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clientes')
    empresas = Empresa.objects.all()
    return render(request, 'atualizar_cliente.html', {'cliente': cliente, 'empresas': empresas})


def deletar_cliente(request, pk):
    cliente = Membro.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success('Cliente deletado com sucesso!')
        return redirect('clientes')
    empresas = Empresa.objects.get(nome=cliente.empresa_cliente)
    return render(request, 'deletar_cliente.html', {'cliente': cliente, 'empresas': empresas})


@login_required
def cliente(request):
    clientes = Membro.objects.all()

    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'clientes.html', {'clientes': clientes, 'page_obj': page_obj})


@login_required
def inserir_tarefas(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        responsavel = request.POST.get('cliente')

        if descricao and responsavel:
            clientes = Membro.objects.get(pk=responsavel)
            # Cria a tarefa associada ao cliente
            tarefa = Tarefa(descricao=descricao, nome_cliente=clientes)
            tarefa.save()

            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('tarefas')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    # Obtém a lista de clientes para exibir no formulário
    clientes = Membro.objects.all()
    return render(request, 'inserir_tarefas.html', {'clientes': clientes})


@login_required
def tarefa(request):
    today = timezone.now().date()
    tarefas = Tarefa.objects.filter(data_realizacao=today)

    paginator = Paginator(tarefas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tarefas.html', {'tarefas': tarefas, 'page_obj': page_obj})


def filtrar_tarefas(request):
    if request.method == 'POST':
        data_pesquisa = request.POST.get('data_pesquisa')
        try:
            tarefas = Tarefa.objects.filter(data_realizacao=data_pesquisa)
            return render(request, 'tarefas.html', {'tarefas': tarefas})
        except ValueError:
            # Handle invalid date format
            return render(request, 'tarefas.html', {'error': 'Data inválida'})
    else:
        # Handle GET request or missing data_pesquisa
        return render(request, 'tarefas.html')


@login_required
def dashboard(request):
    # Obtenha a data atual
    data_atual = date.today()

    # Filtrar tarefas com data igual à data atual
    tarefas_do_dia = Tarefa.objects.filter(data_realizacao=data_atual)

    # Filtrar clientes com aniversário igual à data atual
    clientes_aniversario = Membro.objects.filter(data_aniversario__month=data_atual.month, data_aniversario__day=data_atual.day)

    # Passe os dados filtrados para o template
    return render(request, 'dashboard.html', {'tarefas_do_dia': tarefas_do_dia, 'clientes_aniversario': clientes_aniversario})
