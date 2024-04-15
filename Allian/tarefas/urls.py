from django.urls import path
from . import views
urlpatterns = [
    path('lista/', views.lista_tarefas, name='lista-tarefas'),
    path('adicionar/', views.adicionar_tarefas, name='adicionar-tarefa'),
    path('atualizar/<int:id>/', views.atualizar_tarefa, name='atualizar-tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar-tarefa'),
    path('alterar_status/<int:id>', views.alterar_status, name='alterar-status'),
]
