
from django import forms
from .models import Curso,Entregable,Profesor,Estudiante
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
        email = forms.EmailField(label="Correo Electrónico", required=True)
        password1 = forms.CharField(label="Contraseña",
        widget=forms.PasswordInput)
        password2 = forms.CharField(label="Repetir contraseña",
        widget=forms.PasswordInput)
    
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']


class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso # Vinculación explícita con el modelo físico
        fields = ['nombre', 'camada'] # Columnas expuestas en la interfaz
        # Sobreescritura visual y adición de clases de diseño (Bootstrap)
        labels = {
        'nombre': 'Nombre del Curso',
        'camada': 'Número de Camada'
        }
        widgets = {
    'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Python'}),
    'camada': forms.NumberInput(attrs={'placeholder': 'Ej: 121212'}),
    }


class EntregableModelForm(forms.ModelForm):
    class Meta:
        # Vinculación explícita con el modelo Entregable
        model = Entregable 
        
        # Columnas expuestas en la interfaz
        fields = ['nombre', 'fecha_de_entrega', 'entregado'] 
        
        # Sobreescritura visual de las etiquetas
        labels = {
            'nombre': 'Nombre del Entregable',
            'fecha_de_entrega': 'Fecha de Entrega',
            'entregado': '¿Ya fue entregado?'
        }
        
        # Adición de elementos visuales y placeholders
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Proyecto Final'}),
            'fecha_de_entrega': forms.DateInput(attrs={'type': 'date'}),
            'entregado': forms.CheckboxInput()
        }

class ProfesorModelForm(forms.ModelForm):
    class Meta:
        # Vinculación explícita con el modelo Profesor
        model = Profesor 
        
        # Columnas expuestas en la interfaz
        fields = ['nombre', 'apellido', 'email', 'profesion'] 
        
        # Sobreescritura visual de las etiquetas
        labels = {
            'nombre': 'Nombre del Profesor',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'profesion': 'Profesión / Especialidad'
        }
        
        # Adición de placeholders y controles específicos
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Juan'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ej: Pérez'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ej: juan.perez@email.com'}),
            'profesion': forms.TextInput(attrs={'placeholder': 'Ej: Ingeniero de Software'}),
        }

class EstudianteModelForm(forms.ModelForm):
    class Meta:
        model = Estudiante # Vinculación explícita con el modelo físico
        fields = ['nombre', 'apellido', 'email'] # Columnas expuestas en la interfaz
        
        # Sobreescritura visual y adición de clases de diseño (Bootstrap)
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico'
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Juan'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ej: Pérez'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ej: juan.perez@email.com'}),
        }
