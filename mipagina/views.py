from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from warnings import catch_warnings
from mipagina.forms import FormInput

#It is a dictionary with is envoy the templates
dictionary={'bienvenido':'Hola bienvenido a nuestro sitio web',"image":"reflector1.png","accion":"/mipagina/contacto/"}

#fomulario
"""
@param request: This parameter is the input envoy by the template
@return: This function return one web site and one dictionary by dates
  
"""
def contacto (request):  
    dato1= request.POST['ent1'] # aqui le pedimos al request al dato 'ent1' del formulario
    dictionary['respuesta']=dato1
   # print ("hola")#se imprime en consola para saber si la funcion se esta ejeutando 
    #return render(request,'contacto.html',dic)#renderizamos enviando el diccionario
    return render(request,'index.html',dictionary)

#funcion de llamado

"""
@param request: This parameter is the input envoy by the template
@return: This function return one number with the operation indicate

"""

def fun (request):
    hola='hola mundo, el resultado es:'
    t=str(calcula(1,2,2))
    concatena=hola+t
    retorno='<html><body>%s menos</body></html>'% concatena
    return HttpResponse(retorno)

#calculated

"""
@param request: This parameter is the input envoy by the template, this contains three dates, two 
numbers for do the operation indicate in the third parameter
@return: This function return the response of operation between the two parameters admitted in the form

"""
def calcula(request):
    
    #Assing the variables of entry
    num1 = int(request.POST['Numero_1'])
    num2 = int(request.POST['Numero_2'])
    opc = int(request.POST['operacion'])
    
    #Is the selection of the option
    
    if opc==1:
        total=num1+num2
    elif opc==2:
        total=num1-num2
    elif opc==3:
        total=num1*num2
    elif opc==4:
        try:
            total=num1/num2
        except:
            print ('Error, division por cero')
            total="Error, division por cero"
                
    #Return information
    
    return total

#Called the template index.html

"""
@param request: This parameter is the input envoy by template 
@return: This function return one web site and one dictionary of dates

"""

def solution (request):
    return render(request, 'index.html',dictionary)

def sol2 (request):
    return render(request, 'contacto.html',dictionary)

"""
@param request: This parameter es thi input envoy by template
In this function return the form to the template, and validates the dates admitted
by the user

"""

def formulario(request):
    
    #Cheked the method of the request
    
    if request.method == 'POST':
        
        #Assing the form
        form = FormInput(request.POST)
        
        #Called the function calcula
        
        if form.is_valid():
            rta=calcula(request)
            dictionary['respuesta']=rta
            return render(request,'index.html',dictionary)
    else:
        form=FormInput()       
    dictionary['form']=form
    return render(request,'index.html',dictionary)
