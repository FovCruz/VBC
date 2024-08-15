from django.shortcuts import get_object_or_404, redirect, render

from .models import Tarea
from .forms import TareaForm

# Create your views here.

#LISTAR
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})


#CREAR / AGREGAR
def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')  # Redirigir después de guardar la tarea
    else:
        form = TareaForm()
    
    return render(request, 'editar_tarea.html', {'form': form})

# EDITAR
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'gestion_tareas/editar_tarea.html', {'form': form})

#ELIMINAR
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect('lista_tareas')
    
    return render(request, 'gestion_tareas/confirmar_eliminar.html', {'tarea': tarea})



