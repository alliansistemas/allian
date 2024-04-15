from django.db import models
from django.contrib.auth import get_user_model
from membros.models import Membro

class Tarefa(models.Model):

    STATUS = (
        ('pendente', 'Pendente'),
        ('resolvida', 'Resolvida'),
    )

    atividade = models.TextField()
    data_realizacao = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome_cliente = models.ForeignKey(Membro, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    finalizada = models.CharField(
        max_length=9,
        choices=STATUS,
    )

    def save(self, *args, **kwargs):
        # Convertendo o texto para maiúsculas antes de salvar
        self.atividade = self.atividade.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.atividade