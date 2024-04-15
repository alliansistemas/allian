from django.db import models
from django.contrib.auth import get_user_model
from empresas.models import Empresa

class Membro(models.Model):
    empresa_cliente = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='membros')
    nome = models.CharField(max_length=100)
    data_aniversario = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome