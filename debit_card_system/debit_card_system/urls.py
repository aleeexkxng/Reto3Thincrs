#Urls
from django.urls import path
from debit_card_app import views 

urlpatterns = [
    
    # URLs for Usuario
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:usuario_id>/', views.leer_usuario, name='leer_usuario'),
    path('usuarios/<int:usuario_id>/editar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/<int:usuario_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

        # URLs for Cuenta
    path('usuarios/<int:usuario_id>/cuentas/', views.crear_cuenta, name='crear_cuenta'),
    path('usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/', views.leer_cuenta, name='leer_cuenta'),
    path('usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/editar/', views.actualizar_cuenta, name='actualizar_cuenta'),
    path('usuarios/<int:usuario_id>/cuentas/<int:cuenta_id>/eliminar/', views.eliminar_cuenta, name='eliminar_cuenta'),

]