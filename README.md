# Reto3Thincrs
Reto3 Curso python Thincrs 
# Integrantes:
-Luis Eduardo Mayida Gonzalez
-José Ramon Diaz Lara
-Alejandro Chávez Gómez


Metodos:
  # URLs for Usuario
    Crear usuario - 'usuarios/crear/'
    Leer usuario - 'usuarios/<int:usuario_id>/'
    Editar usuario - 'usuarios/<int:usuario_id>/editar/'
    Eliminar usuario - 'usuarios/<int:usuario_id>/eliminar/'
    
  # URLs for Cuenta

    Crear cuenta - 'usuarios/<int:usuario_id>/cuentas/'
    Leer cuenta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/'
    Editar cuenta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/editar/'
    Eliminar cuenta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/eliminar/'
    
  # URLs for Tarjeta
    Crear Tarjeta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/tarjetas/',
    Leer Tarjeta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/tarjetas/<int:tarjeta_id>/',
    Editar Tarjeta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/tarjetas/<int:tarjeta_id>/editar/',
    Eliminar Tarjeta - 'usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/tarjetas/<int:tarjeta_id>/eliminar/',


