from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='página inicial'),
    path("cadastro/usuário", views.cadastro_usuario, name='cadastro_usuario'),
    path("login", views.login_view, name='login'),
    path("clientes/inserir", views.cadastro_cliente, name='cadastro_cliente'),
    path("clientes/<int:pk>/atualizar/", views.atualizar_cliente, name='atualizar_cliente'),
    path("clientes/<int:pk>/deletar/", views.deletar_cliente, name='deletar_cliente'),
    path("clientes/", views.cliente, name='clientes'),
    path("empresas/", views.empresa, name='empresas'),
    path("empresas/inserir", views.cadastro_empresa, name='cadastro_empresa'),
    path('empresas/<int:pk>/atualizar/', views.atualizar_empresa, name='atualizar_empresa'),
    path('empresas/<int:pk>/deletar/', views.deletar_empresa, name='deletar_empresa'),
    path('tarefas/inserir', views.inserir_tarefas, name='inserir_tarefas'),
    path('tarefas/', views.tarefa, name='tarefas'),
    path('filtrar_tarefas/', views.filtrar_tarefas, name='filtrar_tarefas'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
