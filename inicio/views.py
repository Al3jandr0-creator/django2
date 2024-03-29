from datetime import datetime

# mantener separado lo que traigo de python luego colocamos lo de django y por ultimo lo que venga de nuestro propio proyeto 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Alumno
import random
from inicio.forms import FormularioCreacionAlumno

def inicio(request):
    
    # v1 inicial
    # archivo_abierto = open(r'C:\Users\Pcs4You\56075\Django1\templates\inicio.html', 'r')
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    # dicc ={
    #     'nombre': 'Carlos',
    #     'apellido': 'Perez'
    # }
    # contexto = Context(dicc)
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)
    
    # v2 cargadores
    # template = loader.get_template('inicio.html')
    
    # dicc ={
    #     'nombre': 'Carlos',
    #     'apellido': 'Perez'
    # }

    # template_renderizado = template.render(dicc)
    # return HttpResponse(template_renderizado)

    # v3 - final render
    
    return render(request, 'inicio.html',)

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})

def mostrar_horario(request): 
    fecha = datetime.now()
    return HttpResponse(f'Esta es la fecha y hora actual: {fecha}')

def saludo(request, nombre, apellido):
    nombre_formateado = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f'Bienvenido/a {nombre_formateado} {apellido_formateado}')
 
# def crear_alumno(request, nombre,apellido,edad):
#     alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, nota=random.randint(1, 10))
#     alumno.save()
#     return render(request, 'crear_alumno.html', {'alumno':alumno})

def crear_alumno(request):
    # if request.method == "POST":
        # nombre= request.POST.get('nombre')
        # apellido= request.POST.get('apellido')
        # edad= request.POST.get('edad')
        # alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, nota=random.randint(1, 10))
        # alumno.save()
    if request.method =="POST":
        formulario = FormularioCreacionAlumno(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            edad = formulario.cleaned_data.get('edad')
            nota = nota=random.randint(1, 10)
            alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, nota=nota)
            alumno.save()                       
            return redirect('alumnos')
    formulario = FormularioCreacionAlumno()
    return render(request, 'crear_alumno.html', {'formulario': formulario})