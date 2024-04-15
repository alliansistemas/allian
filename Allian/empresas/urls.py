from django.urls import path
from . import views
from detalhes.views import ListaComputadores, AdicionarComputador, AtualizarComputador, DeletarComputador
urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("empresas/lista/", views.lista_empresas, name='lista-empresas'),
    path('empresas/lista_ajax/', views.lista_empresas_ajax, name='lista_empresas_ajax'),
    path("empresas/adicionar/", views.adicionar_empresa, name='adicionar-empresa'),
    path('empresas/atualizar/<int:id>/', views.atualizar_empresa, name='atualizar-empresa'),
    path('empresas/deletar/<int:id>/', views.deletar_empresa, name='deletar-empresa'),

    path("empresas/lista/<int:id>/computadores/lista/", ListaComputadores, name='lista-computadores'),
    path("empresas/lista/<int:id>/computadores/adicionar/", AdicionarComputador, name='adicionar-computador'),
    path('empresas/lista/<int:id>/computadores/atualizar/<int:pk>/', AtualizarComputador, name='atualizar-computador'),
    path('empresas/lista/<int:id>/computadores/deletar/<int:pk>/', DeletarComputador, name='deletar-computador'),

    path('logout/', views.logout_view, name='logout-view'),
]
