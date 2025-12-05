from django.urls import path
from . import views

app_name = 'nucleo'

urlpatterns = [
    path('', views.kit_ssh, name='kit_ssh'),  # Raíz apunta al kit SSH
    path('kit-ssh/', views.kit_ssh, name='kit_ssh_alt'),  # Ruta alternativa
]
