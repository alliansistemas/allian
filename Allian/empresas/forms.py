from django import forms
from datetime import datetime
from .models import Empresa

class DatePickerWidget(forms.DateInput):
    def __init__(self, *args, **kwargs):
        super(DatePickerWidget, self).__init__(*args, **kwargs)
        self.format = '%d/%m/%y'  # Define o formato de data desejado

    def format_value(self, value):
        if isinstance(value, datetime):
            return value.strftime(self.format)
        return value

class EmpresaForm(forms.ModelForm):
    id_sistema = forms.CharField(label='ID Sistema')
    nome = forms.CharField(label='Nome')
    administrador = forms.CharField(label='Administrador')
    data_certificado = forms.CharField(label='Vencimento Certificado')

    def clean(self):
        cleaned_data = super().clean()

        # Aplicando a conversão para maiúsculas para cada campo
        cleaned_data['id_sistema'] = self.maiusculas(cleaned_data.get('id_sistema'))
        cleaned_data['nome'] = self.maiusculas(cleaned_data.get('nome'))
        cleaned_data['administrador'] = self.maiusculas(cleaned_data.get('administrador'))

        return cleaned_data

    def maiusculas(self, valor):
        if valor:
            return valor.upper()
        return valor

    class Meta:
        model = Empresa
        fields = ('id_sistema', 'nome', 'administrador', 'data_certificado')

