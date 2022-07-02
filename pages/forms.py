from django import forms
from pages.models import FichaVisita, DistritosAdm, Endereco, Info, Equipe
import datetime

class FichaForm(forms.ModelForm):
    class Meta:
        model = FichaVisita
        fields = ['categoria', 'quarto']

class DistritosAdmForm(forms.ModelForm):
    class Meta:
        model = DistritosAdm
        fields = ['distrito_saude', 'bairro', 'municipio']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'complemento', 'numero', 'unidade_federacao']

class InformacoesForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['atividade', 'data', 'hora']
        widgets = {
            'data': forms.DateInput(format= '%Y-%m-%d',attrs={'type': 'date'}),
            'hora': forms.TimeInput(format= '%H:%M',attrs={'type': 'time'})}
        
    def clean_data(self):
        data = self.cleaned_data['data']
        if data > datetime.date.today():
            raise forms.ValidationError('! [Data maior que a data de hoje] !')
        return data
            
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome_agente', 'cargo', 'responsavel']