from django import forms

from pages.models import fichaVisita

class InsereFichaVisita(forms.ModelForm):
    municipio = forms.CharField(
        required=True,
        max_length=255
    )

    localidade = forms.CharField(
        required=True,
        max_length=255
    )

    quarteirao = forms.CharField(
        required=True,
        max_length=255
    )

    distrito = forms.CharField(
        required=True,
        max_length=255
    )

    rua = forms.CharField(
        required=True,
        max_length=255
    )

    numero = forms.IntegerField(
        required=True
    )

    

    class Meta:
        model = fichaVisita

        fields = [
            'municipio',
            'localidade',
            'quarteirao',
            'distrito',
            'rua',
            'numero',
        ]

    