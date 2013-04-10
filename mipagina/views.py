from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from warnings import catch_warnings

diccionary={'bienvenido':'Hola bienvenido a nuestro sitio web',"image":"reflector1.png","accion":"/mipagina/contacto/"}

#fomulario
def contacto (request):  
    dato1= request.POST['ent1'] # aqui le pedimos al request al dato 'ent1' del formulario
    diccionary['respuesta']=dato1
   # print ("hola")#se imprime en consola para saber si la funcion se esta ejeutando 
    #return render(request,'contacto.html',dic)#renderizamos enviando el diccionario
    return render(request,'index.html',diccionary)

#funcion de llamado

def fun (request):
    hola='hola mundo, el resultado es:'
    t=str(calcula(1,2,2))
    concatena=hola+t
    retorno='<html><body>%s menos</body></html>'% concatena
    return HttpResponse(retorno)

#calculadora 

def calcula(request):
    
    #SE ASIGNAN LAS VARIABLES ENVIADAS
    
    num1 = int(request.POST['ent1'])
    num2 = int(request.POST['ent2'])
    opc = int(request.POST['opc'])
    
    #SE HACER LA SELECCION DE LA OPCION
    
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
            
    #SE ASIGNA LA INFORMACION AL DICCIONARIO 
         
    diccionary['respuesta']=str(total)
    
    #SE RETORNA LA INFORMACION
    
    return render(request,'index.html',diccionary)

#Se llama al template index.html
def solution (request):
    return render(request, 'index.html',diccionary)

def sol2 (request):
    return render(request, 'contacto.html',diccionary)
