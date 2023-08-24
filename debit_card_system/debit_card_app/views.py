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

# Views and controllers for Cuenta

def crear_cuenta(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        saldo = request.POST['saldo']
        nueva_cuenta = Cuenta(usuario=usuario, saldo=saldo)
        nueva_cuenta.save()
        return redirect('leer_usuario', usuario_id=usuario.id)
    return render(request, 'crear_cuenta.html', {'usuario': usuario})

def leer_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    return render(request, 'leer_cuenta.html', {'cuenta': cuenta})

def actualizar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    if request.method == 'POST':
        cuenta.saldo = request.POST['saldo']
        cuenta.save()
        return redirect('leer_cuenta', cuenta_id=cuenta.id)
    return render(request, 'actualizar_cuenta.html', {'cuenta': cuenta})

def eliminar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    usuario_id = cuenta.usuario.id
    if request.method == 'POST':
        cuenta.delete()
        return redirect('leer_usuario', usuario_id=usuario_id)
    return render(request, 'eliminar_cuenta.html', {'cuenta': cuenta})
