from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (RegistroView ,
                    HomeView,
                    CursosView,
                    EntregablesView,
                    EstudiantesView,
                    ProfesoresView,
                    CursoUpdateView,
                    CursoDeleteView,
                    CursoCreateView,
                    EntregableCreateView,
                    EntregableDeleteView,
                    EntregableUpdateView,
                    ProfesorCreateView,
                    ProfesorDeleteView,
                    ProfesorUpdateView,
                    EstudianteCreateView,
                    EstudianteDeleteView,
                    EstudianteUpdateView)

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('cursos/', CursosView.as_view(),name='cursos'),
    path('profesores/', ProfesoresView.as_view(),name='profesores'),
    path('entregables/', EntregablesView.as_view(),name='entregables'),
    path('estudiantes/', EstudiantesView.as_view(),name='estudiantes'),

    path('cursos/editar/<int:pk>/', CursoUpdateView.as_view(), name='editar_curso'),
    path('cursos/borrar/<int:pk>/', CursoDeleteView.as_view(), name='borrar_curso'),
    path('cursos/crear/', CursoCreateView.as_view(), name='crear_curso'),

    path('entregables/editar/<int:pk>/', EntregableUpdateView.as_view(), name='editar_entregable'),
    path('entregables/borrar/<int:pk>/', EntregableDeleteView.as_view(), name='borrar_entregable'),
    path('entregables/crear/', EntregableCreateView.as_view(), name='crear_entregable'),

    path('profesores/editar/<int:pk>/', ProfesorUpdateView.as_view(), name='editar_profesor'),
    path('profesores/borrar/<int:pk>/', ProfesorDeleteView.as_view(), name='borrar_profesor'),
    path('profesores/crear/', ProfesorCreateView.as_view(), name='crear_profesor'),


    path('estudiantes/editar/<int:pk>/', EstudianteUpdateView.as_view(), name='editar_estudiante'),
    path('estudiantes/borrar/<int:pk>/', EstudianteDeleteView.as_view(), name='borrar_estudiante'),
    path('estudiantes/crear/', EstudianteCreateView.as_view(), name='crear_estudiante'),

    path(
 'login/',
 LoginView.as_view(template_name='login.html'),
 name='login'
 ),
path(
 'logout/',
 LogoutView.as_view(),
 name='logout'
 ),
 path(
 'registro/',
 RegistroView.as_view(),
 name='registro'
 ),


]
