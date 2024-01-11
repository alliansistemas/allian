from django.contrib import admin
from .models import Empresa, Membro, Tarefa

admin.site.register(Empresa)
admin.site.register(Membro)
admin.site.register(Tarefa)
