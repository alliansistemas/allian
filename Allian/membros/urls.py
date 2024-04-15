from django.urls import path
from . import views
urlpatterns = [
    path("lista/", views.lista_membros, name='lista-membros'),
    path("lista_ajax/", views.lista_membros_ajax, name='lista_membros_ajax'),
    path("adicionar/", views.adicionar_membro, name='adicionar-membro'),
    path("atualizar/<int:id>/", views.atualizar_membro, name='atualizar-membro'),
    path("deletar/<int:id>/", views.deletar_membro, name='deletar-membro'),
]
