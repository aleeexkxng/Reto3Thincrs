#Urls
from django.urls import path
from debit_card_app import views 

urlpatterns = [
    
    # URLs for Usuario
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:usuario_id>/', views.leer_usuario, name='leer_usuario'),
    path('usuarios/<int:usuario_id>/editar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/<int:usuario_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

]