# Generated by Django 5.0.1 on 2024-02-24 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0003_rename_empresa_detalhescomputador_empresa_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="detalhescomputador",
            old_name="empresa_id",
            new_name="empresa",
        ),
    ]