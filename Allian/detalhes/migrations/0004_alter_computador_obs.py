# Generated by Django 5.0.1 on 2024-03-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("detalhes", "0003_computador_data_manutencao_computador_obs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computador",
            name="obs",
            field=models.CharField(max_length=100, verbose_name="Observações"),
        ),
    ]
