from django import forms
from .models import Moneda, BancoLibrador, Estado, ChEmitidos, ChRecibidos

class MonedaForm(forms.ModelForm):
    class Meta:
        model = Moneda
        fields = ['nombre', 'simbolo']

class BancoLibradorForm(forms.ModelForm):
    class Meta:
        model = BancoLibrador
        fields = ['nombre']

class EstadodeChequeForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']

class ChequesEmitidosForm(forms.ModelForm):
    class Meta:
        model = ChEmitidos
        fields = '__all__'

class ChequesRecibidosForm(forms.ModelForm):
    class Meta:
        model = ChRecibidos
        fields = '__all__'
