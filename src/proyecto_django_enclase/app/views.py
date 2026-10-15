from django.shortcuts import render
from django.views import View
from .models import Curso,Entregable,Profesor,Estudiante
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CursoModelForm,EntregableModelForm,ProfesorModelForm,EstudianteModelForm,UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistroView(CreateView):
 form_class = UserRegisterForm
 template_name = 'registro.html'
 success_url = reverse_lazy('login') 


class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        productos = [
    {"id": 1, "nombre": "Laptop Asus", "precio": 850.00, "categoria": "Tecnología"},
    {"id": 2, "nombre": "Teclado Mecánico", "precio": 45.50, "categoria": "Accesorios"},
    {"id": 3, "nombre": "Monitor 24' Dell", "precio": 180.00, "categoria": "Tecnología"},
    {"id": 4, "nombre": "Ratón Inalámbrico", "precio": 25.00, "categoria": "Accesorios"},
    {"id": 5, "nombre": "Auriculares Sony", "precio": 90.00, "categoria": "Audio"}
]
        contexto=dict(titulo="Home",mensaje="Esta es la pagina de inicio en Django",productos=productos)

        return render(request,"index.html",contexto)



class CursosView(LoginRequiredMixin,View):
    def get(self,request):
        contexto=dict(titulo="Cursos",mensaje="Esta es la pagina de inicio de los Cursos",cursos=Curso.objects.all())

        return render(request,"lista_cursos.html",contexto)
    
class CursoCreateView(LoginRequiredMixin,CreateView):
    model = Curso
    form_class = CursoModelForm
    template_name = 'cursos.html'        
    success_url = reverse_lazy('cursos')

class CursoUpdateView(LoginRequiredMixin,UpdateView):
    model = Curso
    form_class = CursoModelForm
    template_name = 'cursos.html' 
    success_url = reverse_lazy('cursos')


# === DELETE (Borrar) ===
class CursoDeleteView(LoginRequiredMixin,DeleteView):
    model = Curso
    template_name = 'curso_confirm_delete.html' # Este archivo lo crearemos ahora
    success_url = reverse_lazy('cursos')


class EstudiantesView(LoginRequiredMixin,View):
    def get(self,request):
        contexto=dict(titulo="Estudiantes",mensaje="Esta es la pagina de inicio de los Estudiantes",estudiantes=Estudiante.objects.all())

        return render(request,"lista_estudiantes.html",contexto)



# === READ (Listado de Entregables) ===
class EntregablesView(LoginRequiredMixin,View):
    def get(self, request):
        contexto = dict(
            titulo="Entregables",
            mensaje="Esta es la página de inicio de los Entregables",
            entregables=Entregable.objects.all()
        )
        return render(request, "lista_entregables.html", contexto)
    
# === CREATE (Crear Entregable) ===
class EntregableCreateView(LoginRequiredMixin,CreateView):
    model = Entregable
    form_class = EntregableModelForm
    template_name = 'entregables.html'        
    success_url = reverse_lazy('entregables')  # Nombre del path en tus urls.py

# === UPDATE (Editar Entregable) ===
class EntregableUpdateView(LoginRequiredMixin,UpdateView):
    model = Entregable
    form_class = EntregableModelForm
    template_name = 'entregables.html' 
    success_url = reverse_lazy('entregables')

# === DELETE (Borrar Entregable) ===
class EntregableDeleteView(LoginRequiredMixin,DeleteView):
    model = Entregable
    template_name = 'entregable_confirm_delete.html' 
    success_url = reverse_lazy('entregables')



# === READ (Listado de Profesores) ===
class ProfesoresView(LoginRequiredMixin,View):
    def get(self, request):
        contexto = dict(
            titulo="Profesores",
            mensaje="Esta es la página de inicio de los Profesores",
            profesores=Profesor.objects.all()
        )
        return render(request, "lista_profesores.html", contexto)
    
# === CREATE (Crear Profesor) ===
class ProfesorCreateView(LoginRequiredMixin,CreateView):
    model = Profesor
    form_class = ProfesorModelForm
    template_name = 'profesores.html'        
    success_url = reverse_lazy('profesores')  # Nombre del path en urls.py

# === UPDATE (Editar Profesor) ===
class ProfesorUpdateView(LoginRequiredMixin,UpdateView):
    model = Profesor
    form_class = ProfesorModelForm
    template_name = 'profesores.html' 
    success_url = reverse_lazy('profesores')

# === DELETE (Borrar Profesor) ===
class ProfesorDeleteView(LoginRequiredMixin,DeleteView):
    model = Profesor
    template_name = 'profesor_confirm_delete.html' 
    success_url = reverse_lazy('profesores')


    # === CREATE (Crear) ===
class EstudianteCreateView(LoginRequiredMixin,CreateView):
    model = Estudiante
    form_class = EstudianteModelForm
    template_name = 'estudiantes.html'        # ← Template para el Formulario de creación
    success_url = reverse_lazy('estudiantes')

# === UPDATE (Editar) ===
class EstudianteUpdateView(LoginRequiredMixin,UpdateView):
    model = Estudiante
    form_class = EstudianteModelForm
    template_name = 'estudiantes.html'        # ← Reutiliza el formulario inteligente
    success_url = reverse_lazy('estudiantes')

# === DELETE (Borrar) ===
class EstudianteDeleteView(LoginRequiredMixin,DeleteView):
    model = Estudiante
    template_name = 'estudiante_confirm_delete.html' # Template de confirmación de borrado
    success_url = reverse_lazy('estudiantes')
