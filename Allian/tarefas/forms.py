from django import forms

from .models import Tarefa
from membros.models import Membro

class TarefaForm(forms.ModelForm):
    nome_cliente = forms.ModelChoiceField(
        label='Membro ou Responsável',
        queryset=Membro.objects.all()
    )

    class Meta:
        model = Tarefa
        fields = ('atividade', 'nome_cliente')