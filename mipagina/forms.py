#encoding:utf-8
from django import forms
from django.forms import ModelForm

#ATRIBUTES

operation=(('1','SUMA'),('2','RESTA'),('3','PRODUCTO'),('4','DIVISION'))
#METHODS

#FormInput: This form get three inputs, two numbers and one operation, this is indicate by a number
"""
@return: Return one number with the operation indicate
 
"""
class FormInput(forms.Form):
    
    #Is created the form
    
    Numero_1 = forms.DecimalField()#First number
    Numero_2 = forms.DecimalField()#Second number
    operacion = forms.ChoiceField(choices=operation)#Options whit indicate the operation
    