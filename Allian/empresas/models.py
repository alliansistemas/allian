from django.db import models
from django.contrib.auth import get_user_model

class Empresa(models.Model):
    id_sistema = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    administrador = models.CharField(max_length=100)
    data_certificado = models.CharField(max_length=10, verbose_name="Vencimento do Certificado")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome