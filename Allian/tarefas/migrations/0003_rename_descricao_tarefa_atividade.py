# Generated by Django 5.0.1 on 2024-01-25 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0002_alter_tarefa_descricao"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tarefa",
            old_name="descricao",
            new_name="atividade",
        ),
    ]
