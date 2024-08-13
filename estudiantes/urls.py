from django.urls import path
from .views import MiHome, EstudianteLista, EstudianteView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView

urlpatterns = [
    path("home/", MiHome.as_view(), name='ver_home'),
    path("estudiantes/", EstudianteLista.as_view(), name='ver_estudiantes'),
    path("estudiante/<str:pk>", EstudianteView.as_view(), name='ver_estudiante'),
    path("crear/", EstudianteCreateView.as_view(), name='crear'),
    path("actualizar/<str:pk>", EstudianteUpdateView.as_view(), name='actualizar'),
    path("borrar/<str:pk>", EstudianteDeleteView.as_view(), name='borrar'),
]
