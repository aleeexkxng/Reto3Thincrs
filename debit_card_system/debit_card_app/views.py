from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Cuenta, Tarjeta


def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nuevo_usuario = Usuario(nombre=nombre)
        nuevo_usuario.save()
        return redirect('leer_usuario', usuario_id=nuevo_usuario.id)
    # Create a corresponding template
    return render(request, 'crear_usuario.html')


def leer_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    # Create a corresponding template
    return render(request, 'leer_usuario.html', {'usuario': usuario})


def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.save()
        return redirect('leer_usuario', usuario_id=usuario.id)
    # Create a corresponding template
    return render(request, 'actualizar_usuario.html', {'usuario': usuario})


def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    # Create a corresponding template
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})

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

# Views and controllers for Tarjeta


def crear_tarjeta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    if request.method == 'POST':
        balance = request.POST['balance']
        nueva_tarjeta = Tarjeta(cuenta=cuenta, balance=balance)
        nueva_tarjeta.save()
        return redirect('leer_cuenta', cuenta_id=cuenta.id)
    return render(request, 'crear_tarjeta.html', {'cuenta': cuenta})


def leer_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    return render(request, 'leer_tarjeta.html', {'tarjeta': tarjeta})


def actualizar_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    if request.method == 'POST':
        tarjeta.balance = request.POST['balance']
        tarjeta.save()
        return redirect('leer_tarjeta', tarjeta_id=tarjeta.id)
    return render(request, 'actualizar_tarjeta.html', {'tarjeta': tarjeta})


def eliminar_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    cuenta_id = tarjeta.cuenta.id
    if request.method == 'POST':
        tarjeta.delete()
        return redirect('leer_cuenta', cuenta_id=cuenta_id)
    return render(request, 'eliminar_tarjeta.html', {'tarjeta': tarjeta})
