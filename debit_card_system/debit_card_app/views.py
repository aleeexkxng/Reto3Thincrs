from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Cuenta, Tarjeta

def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nuevo_usuario = Usuario(nombre=nombre)
        nuevo_usuario.save()
        return redirect('leer_usuario', usuario_id=nuevo_usuario.id)
    return render(request, 'crear_usuario.html')  # Create a corresponding template

def leer_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'leer_usuario.html', {'usuario': usuario})  # Create a corresponding template

def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.save()
        return redirect('leer_usuario', usuario_id=usuario.id)
    return render(request, 'actualizar_usuario.html', {'usuario': usuario})  # Create a corresponding template

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})  # Create a corresponding template
