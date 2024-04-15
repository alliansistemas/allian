from django import forms
from empresas.models import Empresa
from .models import Membro

class MembroForm(forms.ModelForm):
    nome = forms.CharField(label='Nome')
    empresa_cliente = forms.ModelChoiceField(
        label='Empresa',
        queryset=Empresa.objects.all()
    )
    data_aniversario = forms.DateField(label='Data de Aniversário', widget=forms.DateInput(format='%d-%m-%Y'), input_formats=['%d-%m-%Y'])

    def clean(self):
        cleaned_data = super().clean()

        # Aplicando a conversão para maiúsculas para cada campo
        cleaned_data['nome'] = self.maiusculas(cleaned_data.get('nome'))

        return cleaned_data

    def maiusculas(self, valor):
        if valor:
            return valor.upper()
        return valor

    class Meta:
        model = Membro
        fields = ('nome', 'empresa_cliente', 'data_aniversario')
