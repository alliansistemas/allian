from django import forms
from .models import Tarefa
from membros.models import Membro

class TarefaForm(forms.ModelForm):
    nome_cliente = forms.ModelChoiceField(
        label='Membro ou Responsável',
        queryset=Membro.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    colaborador = forms.ChoiceField(
        label="Colaborador",
        choices=(
            ('RUAN', 'RUAN'),
            ('THIAGO', 'THIAGO'),
            # Repita as mesmas opções do modelo para consistência
        ),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'type': 'checkbox-list',
        })
    )

    class Meta:
        model = Tarefa
        fields = ('atividade', 'nome_cliente', 'colaborador')
