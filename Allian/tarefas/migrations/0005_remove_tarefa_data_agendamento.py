# Generated by Django 5.0.1 on 2024-02-15 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0004_tarefa_data_agendamento"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tarefa",
            name="data_agendamento",
        ),
    ]