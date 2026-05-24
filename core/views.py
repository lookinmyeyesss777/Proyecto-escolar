# ==========================
# IMPORTS AL INICIO
# ==========================
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Importamos TODOS los modelos, asegurándonos de traer los nuevos
from .models import Profesor, Estudiante, Materia, Carrera, Aula, Grupo, PeriodoSemestral, Horario

# ==========================
# CRUD PERIODO SEMESTRAL
# ==========================
class PeriodoSemestralListView(ListView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_list.html'
    context_object_name = 'periodos'

class PeriodoSemestralCreateView(CreateView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_form.html'
    fields = ['nombre', 'fecha_inicio', 'fecha_fin']
    success_url = reverse_lazy('periodosemestral_list')

class PeriodoSemestralUpdateView(UpdateView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_form.html'
    fields = ['nombre', 'fecha_inicio', 'fecha_fin']
    success_url = reverse_lazy('periodosemestral_list')

class PeriodoSemestralDeleteView(DeleteView):
    model = PeriodoSemestral
    template_name = 'core/periodosemestral_confirm_delete.html'
    success_url = reverse_lazy('periodosemestral_list')

def inicio(request):
    return render(request, 'core/inicio.html')

# ==========================
# CRUD CARRERA
# ==========================
class CarreraListView(ListView):
    model = Carrera
    template_name = 'core/carrera_list.html'
    context_object_name = 'carreras'

class CarreraCreateView(CreateView):
    model = Carrera
    template_name = 'core/carrera_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('carrera_list')

class CarreraUpdateView(UpdateView):
    model = Carrera
    template_name = 'core/carrera_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('carrera_list')

class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'core/carrera_confirm_delete.html'
    success_url = reverse_lazy('carrera_list')

# ==========================
# CRUD HORARIO
# ==========================
class HorarioListView(ListView):
    model = Horario
    template_name = 'core/horario_list.html'
    context_object_name = 'horarios'

class HorarioCreateView(CreateView):
    model = Horario
    template_name = 'core/horario_form.html'
    fields = ['dias', 'hora_inicio', 'hora_fin']
    success_url = reverse_lazy('horario_list')

class HorarioUpdateView(UpdateView):
    model = Horario
    template_name = 'core/horario_form.html'
    fields = ['dias', 'hora_inicio', 'hora_fin']
    success_url = reverse_lazy('horario_list')

class HorarioDeleteView(DeleteView):
    model = Horario
    template_name = 'core/horario_confirm_delete.html'
    success_url = reverse_lazy('horario_list')

# ==========================
# CRUD AULA
# ==========================
class AulaListView(ListView):
    model = Aula
    template_name = 'core/aula_list.html'
    context_object_name = 'aulas'

class AulaCreateView(CreateView):
    model = Aula
    template_name = 'core/aula_form.html'
    fields = ['nombre', 'capacidad', 'ubicacion'] # Solucionado: Se agregó capacidad
    success_url = reverse_lazy('aula_list')

class AulaUpdateView(UpdateView):
    model = Aula
    template_name = 'core/aula_form.html'
    fields = ['nombre', 'capacidad', 'ubicacion']
    success_url = reverse_lazy('aula_list')

class AulaDeleteView(DeleteView):
    model = Aula
    template_name = 'core/aula_confirm_delete.html'
    success_url = reverse_lazy('aula_list')

# ==========================
# CRUD MATERIA
# ==========================
class MateriaListView(ListView):
    model = Materia
    template_name = 'core/materia_list.html'
    context_object_name = 'materias'

class MateriaCreateView(CreateView):
    model = Materia
    template_name = 'core/materia_form.html'
    fields = ['clave', 'nombre', 'creditos', 'carrera'] # Solucionado: Se agregó créditos
    success_url = reverse_lazy('materia_list')

class MateriaUpdateView(UpdateView):
    model = Materia
    template_name = 'core/materia_form.html'
    fields = ['clave', 'nombre', 'creditos', 'carrera']
    success_url = reverse_lazy('materia_list')

class MateriaDeleteView(DeleteView):
    model = Materia
    template_name = 'core/materia_confirm_delete.html'
    success_url = reverse_lazy('materia_list')

# ==========================
# CRUD PROFESOR
# ==========================
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'core/profesor_list.html'
    context_object_name = 'profesores'

class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = 'core/profesor_form.html'
    fields = ['nombre', 'apellidos', 'email', 'telefono'] # Solucionado: apellido cambió a apellidos
    success_url = reverse_lazy('profesor_list')

class ProfesorUpdateView(UpdateView):
    model = Profesor
    template_name = 'core/profesor_form.html'
    fields = ['nombre', 'apellidos', 'email', 'telefono']
    success_url = reverse_lazy('profesor_list')

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'core/profesor_confirm_delete.html'
    success_url = reverse_lazy('profesor_list')

# ==========================
# CRUD ESTUDIANTE
# ==========================
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'core/estudiante_list.html'
    context_object_name = 'estudiantes'

class EstudianteCreateView(CreateView):
    model = Estudiante
    template_name = 'core/estudiante_form.html'
    fields = ['matricula', 'nombre', 'apellidos', 'email', 'carrera'] # Solucionado: Se quitó el grupo
    success_url = reverse_lazy('estudiante_list')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = 'core/estudiante_form.html'
    fields = ['matricula', 'nombre', 'apellidos', 'email', 'carrera']
    success_url = reverse_lazy('estudiante_list')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'core/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante_list')

# ==========================
# CRUD GRUPO
# ==========================
class GrupoListView(ListView):
    model = Grupo
    template_name = 'core/grupo_list.html'
    context_object_name = 'grupos'

class GrupoCreateView(CreateView):
    model = Grupo
    template_name = 'core/grupo_form.html'
    # Solucionado: Se incluyeron todas las llaves foráneas exigidas por tu rúbrica
    fields = ['nombre', 'profesor', 'materia', 'aula', 'periodo', 'horario', 'estudiantes']
    success_url = reverse_lazy('grupo_list')

class GrupoUpdateView(UpdateView):
    model = Grupo
    template_name = 'core/grupo_form.html'
    fields = ['nombre', 'profesor', 'materia', 'aula', 'periodo', 'horario', 'estudiantes']
    success_url = reverse_lazy('grupo_list')

class GrupoDeleteView(DeleteView):
    model = Grupo
    template_name = 'core/grupo_confirm_delete.html'
    success_url = reverse_lazy('grupo_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Grupo, Calificacion, Estudiante

def capturar_calificaciones(request, grupo_id):
    # 1. Buscamos el grupo de la base de datos usando su ID
    grupo = get_object_or_404(Grupo, id=grupo_id)
    
    # 2. Traemos a todos los estudiantes inscritos en este grupo específico
    estudiantes = grupo.estudiantes.all()

    if request.method == 'POST':
        # Si el usuario presionó "Guardar"
        for estudiante in estudiantes:
            # Buscamos el valor del input que corresponde a este estudiante
            nombre_input = f"calif_{estudiante.id}"
            valor_calificacion = request.POST.get(nombre_input)

            if valor_calificacion:
                # update_or_create busca si ya existe la calificación para actualizarla,
                # y si no existe, crea un registro nuevo.
                Calificacion.objects.update_or_create(
                    estudiante=estudiante,
                    grupo=grupo,
                    materia=grupo.materia,   # Viene automático desde el grupo
                    periodo=grupo.periodo,   # Viene automático desde el grupo
                    defaults={'valor': valor_calificacion} # El número final (ej: 85)
                )
        
        # Al terminar de guardar, redirige a la lista de grupos
        return redirect('grupo_list')

    # Si solo está cargando la página (GET), renderiza el HTML pasándole el grupo y los alumnos
    return render(request, 'core/captura_calificaciones.html', {
        'grupo': grupo,
        'estudiantes': estudiantes
    })