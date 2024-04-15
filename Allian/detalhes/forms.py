from django import forms
from .models import Computador

class ComputadorForm(forms.ModelForm):
    nome_computador = forms.CharField(label='Nome do Computador')
    numero_anydesk = forms.CharField(label='Numeração do AnyDesk')

    def clean(self):
        cleaned_data = super().clean()

        # Aplicando a conversão para maiúsculas para cada campo
        cleaned_data['nome_computador'] = self.maiusculas(cleaned_data.get('nome_computador'))
        cleaned_data['numero_anydesk'] = self.maiusculas(cleaned_data.get('numero_anydesk'))

        return cleaned_data

    def maiusculas(self, valor):
        if valor:
            return valor.upper()
        return valor

    class Meta:
        model = Computador
        fields = ["nome_computador", "numero_anydesk", "obs"]