# Generated by Django 5.0.1 on 2024-02-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0003_rename_descricao_tarefa_atividade"),
    ]

    operations = [
        migrations.AddField(
            model_name="tarefa",
            name="data_agendamento",
            field=models.DateField(blank=True, null=True),
        ),
    ]
