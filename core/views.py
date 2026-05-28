# ==========================
# IMPORTS AL INICIO
# ==========================
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# --- IMPORTS DE SEGURIDAD (NUEVO) ---
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Importamos TODOS los modelos
from .models import Profesor, Estudiante, Materia, Carrera, Aula, Grupo, PeriodoSemestral, Horario, Calificacion

# ==========================
# VISTA DE INICIO (Función)
# ==========================
@login_required
def inicio(request):
    return render(request, 'core/inicio.html')

# ==========================
# CRUD PERIODO SEMESTRAL (Clases)
# ==========================
class PeriodoSemestralListView(LoginRequiredMixin, ListView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_list.html'
    context_object_name = 'periodos'

class PeriodoSemestralCreateView(LoginRequiredMixin, CreateView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_form.html'
    fields = ['nombre', 'fecha_inicio', 'fecha_fin']
    success_url = reverse_lazy('periodosemestral_list')

class PeriodoSemestralUpdateView(LoginRequiredMixin, UpdateView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_form.html'
    fields = ['nombre', 'fecha_inicio', 'fecha_fin']
    success_url = reverse_lazy('periodosemestral_list')

class PeriodoSemestralDeleteView(LoginRequiredMixin, DeleteView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_confirm_delete.html'
    success_url = reverse_lazy('periodosemestral_list')

# ==========================
# CRUD CARRERA
# ==========================
class CarreraListView(LoginRequiredMixin, ListView):
    model = Carrera
    template_name = 'core/carrera_list.html'
    context_object_name = 'carreras'

class CarreraCreateView(LoginRequiredMixin, CreateView):
    model = Carrera
    template_name = 'core/carrera_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('carrera_list')

class CarreraUpdateView(LoginRequiredMixin, UpdateView):
    model = Carrera
    template_name = 'core/carrera_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('carrera_list')

class CarreraDeleteView(LoginRequiredMixin, DeleteView):
    model = Carrera
    template_name = 'core/carrera_confirm_delete.html'
    success_url = reverse_lazy('carrera_list')

# ==========================
# CRUD HORARIO
# ==========================
class HorarioListView(LoginRequiredMixin, ListView):
    model = Horario
    template_name = 'core/horario_list.html'
    context_object_name = 'horarios'

class HorarioCreateView(LoginRequiredMixin, CreateView):
    model = Horario
    template_name = 'core/horario_form.html'
    fields = ['dias', 'hora_inicio', 'hora_fin']
    success_url = reverse_lazy('horario_list')

class HorarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Horario
    template_name = 'core/horario_form.html'
    fields = ['dias', 'hora_inicio', 'hora_fin']
    success_url = reverse_lazy('horario_list')

class HorarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Horario
    template_name = 'core/horario_confirm_delete.html'
    success_url = reverse_lazy('horario_list')

# ==========================
# CRUD AULA
# ==========================
class AulaListView(LoginRequiredMixin, ListView):
    model = Aula
    template_name = 'core/aula_list.html'
    context_object_name = 'aulas'

class AulaCreateView(LoginRequiredMixin, CreateView):
    model = Aula
    template_name = 'core/aula_form.html'
    fields = ['nombre', 'capacidad', 'ubicacion']
    success_url = reverse_lazy('aula_list')

class AulaUpdateView(LoginRequiredMixin, UpdateView):
    model = Aula
    template_name = 'core/aula_form.html'
    fields = ['nombre', 'capacidad', 'ubicacion']
    success_url = reverse_lazy('aula_list')

class AulaDeleteView(LoginRequiredMixin, DeleteView):
    model = Aula
    template_name = 'core/aula_confirm_delete.html'
    success_url = reverse_lazy('aula_list')

# ==========================
# CRUD MATERIA
# ==========================
class MateriaListView(LoginRequiredMixin, ListView):
    model = Materia
    template_name = 'core/materia_list.html'
    context_object_name = 'materias'

class MateriaCreateView(LoginRequiredMixin, CreateView):
    model = Materia
    template_name = 'core/materia_form.html'
    fields = ['clave', 'nombre', 'creditos', 'carrera']
    success_url = reverse_lazy('materia_list')

class MateriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Materia
    template_name = 'core/materia_form.html'
    fields = ['clave', 'nombre', 'creditos', 'carrera']
    success_url = reverse_lazy('materia_list')

class MateriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Materia
    template_name = 'core/materia_confirm_delete.html'
    success_url = reverse_lazy('materia_list')

# ==========================
# CRUD PROFESOR
# ==========================
class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = 'core/profesor_list.html'
    context_object_name = 'profesores'

class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    template_name = 'core/profesor_form.html'
    fields = ['nombre', 'apellidos', 'email', 'telefono']
    success_url = reverse_lazy('profesor_list')

class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    template_name = 'core/profesor_form.html'
    fields = ['nombre', 'apellidos', 'email', 'telefono']
    success_url = reverse_lazy('profesor_list')

class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    template_name = 'core/profesor_confirm_delete.html'
    success_url = reverse_lazy('profesor_list')

# ==========================
# CRUD ESTUDIANTE
# ==========================
class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'core/estudiante_list.html'
    context_object_name = 'estudiantes'

class EstudianteCreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    template_name = 'core/estudiante_form.html'
    fields = ['matricula', 'nombre', 'apellidos', 'email', 'carrera']
    success_url = reverse_lazy('estudiante_list')

class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    template_name = 'core/estudiante_form.html'
    fields = ['matricula', 'nombre', 'apellidos', 'email', 'carrera']
    success_url = reverse_lazy('estudiante_list')

class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = 'core/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante_list')

# ==========================
# CRUD GRUPO
# ==========================
class GrupoListView(LoginRequiredMixin, ListView):
    model = Grupo
    template_name = 'core/grupo_list.html'
    context_object_name = 'grupos'

class GrupoCreateView(LoginRequiredMixin, CreateView):
    model = Grupo
    template_name = 'core/grupo_form.html'
    fields = ['nombre', 'profesor', 'materia', 'aula', 'periodo', 'horario', 'estudiantes']
    success_url = reverse_lazy('grupo_list')

class GrupoUpdateView(LoginRequiredMixin, UpdateView):
    model = Grupo
    template_name = 'core/grupo_form.html'
    fields = ['nombre', 'profesor', 'materia', 'aula', 'periodo', 'horario', 'estudiantes']
    success_url = reverse_lazy('grupo_list')

class GrupoDeleteView(LoginRequiredMixin, DeleteView):
    model = Grupo
    template_name = 'core/grupo_confirm_delete.html'
    success_url = reverse_lazy('grupo_list')

# ==========================
# CAPTURA DE CALIFICACIONES (Función)
# ==========================
@login_required
def capturar_calificaciones(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    estudiantes = grupo.estudiantes.all()

    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante_id')
        valor_calificacion = request.POST.get('calificacion')
        
        if estudiante_id and valor_calificacion is not None:
            estudiante_obj = get_object_or_404(Estudiante, id=estudiante_id)
            
            Calificacion.objects.update_or_create(
                estudiante=estudiante_obj,
                grupo=grupo,
                materia=grupo.materia,
                periodo=grupo.periodo,
                defaults={'valor': valor_calificacion}
            )
        
        return redirect('capturar_calificaciones', grupo_id=grupo.id)

    for estudiante in estudiantes:
        calif_existente = Calificacion.objects.filter(estudiante=estudiante, grupo=grupo).first()
        if calif_existente:
            estudiante.calificacion_actual = calif_existente.valor
        else:
            estudiante.calificacion_actual = ""

    return render(request, 'core/captura_calificaciones.html', {
        'grupo': grupo,
        'estudiantes': estudiantes,
    })