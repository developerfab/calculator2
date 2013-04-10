from django import forms

class FormularioContacto(forms.Form):
    
    #Se crea  el dato en el espacio del formulario
    
    dato = forms.CharField(max_length=10)
    cc = forms.BooleanField(required=False)
    