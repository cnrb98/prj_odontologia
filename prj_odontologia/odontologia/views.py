from django.shortcuts import render,redirect
from .models import Persona
from .forms import PersonaForm


def index(request, template_name='odontologia/index.html'):
    return render(request, template_name)

def personas_listar(request, template_name='odontologia/personas.html'):
    personas = Persona.objects.all()
    dato_personas = {"personas": personas}
    return render(request, template_name, dato_personas)

def nueva_persona(request, template_name='odontologia/persona_form.html'):
    if request.method=='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato = {"form":form}
    return render(request, template_name, dato)

def modificar_persona(request, pk, template_name='odontologia/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)

def eliminar_persona(request, pk, template_name='odontologia/persona_confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personas')
    else:
        dato = {'form':persona}
        return render(request, template_name, dato)


