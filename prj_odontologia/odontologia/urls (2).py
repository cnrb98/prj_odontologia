from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personas", views.personas_listar, name="personas"),
    path("nueva_persona", views.nueva_persona, name="nueva_persona"),
    path("modificar_persona/<int:pk>", views.modificar_persona, name="modificar_persona"),
    path("eliminar_persona/<int:pk>", views.eliminar_persona, name="eliminar_persona")
]