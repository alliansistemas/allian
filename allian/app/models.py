from django.db import models


class Empresa(models.Model):
    objects = None
    id_sistema = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    administrador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Membro(models.Model):
    objects = None
    empresa_cliente = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='membros')
    nome = models.CharField(max_length=100)
    data_aniversario = models.DateField()

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    objects = None
    descricao = models.CharField(max_length=100)
    data_realizacao = models.DateField(auto_now_add=True)
    nome_cliente = models.ForeignKey(Membro, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
