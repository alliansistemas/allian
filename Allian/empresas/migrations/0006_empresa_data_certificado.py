# Generated by Django 5.0.1 on 2024-04-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0005_delete_detalhescomputador"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresa",
            name="data_certificado",
            field=models.CharField(
                default=1, max_length=10, verbose_name="Vencimento do Certificado"
            ),
            preserve_default=False,
        ),
    ]