from django.db import models
from empresas.models import Empresa
from django.contrib.auth import get_user_model


# Create your models here.
class Computador(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome_computador = models.CharField(max_length=50)
    numero_anydesk = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_manutencao = models.DateTimeField(auto_now_add=True)
    obs = models.TextField()

    def __str__(self):
        return f"{self.empresa.nome} - {self.nome_computador} ({self.numero_anydesk})"