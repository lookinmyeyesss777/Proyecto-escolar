
from django.urls import path
from . import views

urlpatterns = [
    path('periodos/', views.PeriodoSemestralListView.as_view(), name='periodosemestral_list'),
    path('periodos/nuevo/', views.PeriodoSemestralCreateView.as_view(), name='periodosemestral_create'),
    path('periodos/<int:pk>/editar/', views.PeriodoSemestralUpdateView.as_view(), name='periodosemestral_update'),
    path('periodos/<int:pk>/eliminar/', views.PeriodoSemestralDeleteView.as_view(), name='periodosemestral_delete'),
    path('horarios/', views.HorarioListView.as_view(), name='horario_list'),
    path('horarios/nuevo/', views.HorarioCreateView.as_view(), name='horario_create'),
    path('horarios/<int:pk>/editar/', views.HorarioUpdateView.as_view(), name='horario_update'),
    path('horarios/<int:pk>/eliminar/', views.HorarioDeleteView.as_view(), name='horario_delete'),
    path('carreras/', views.CarreraListView.as_view(), name='carrera_list'),
    path('carreras/nuevo/', views.CarreraCreateView.as_view(), name='carrera_create'),
    path('carreras/<int:pk>/editar/', views.CarreraUpdateView.as_view(), name='carrera_update'),
    path('carreras/<int:pk>/eliminar/', views.CarreraDeleteView.as_view(), name='carrera_delete'),
    path('aulas/', views.AulaListView.as_view(), name='aula_list'),
    path('aulas/nuevo/', views.AulaCreateView.as_view(), name='aula_create'),
    path('aulas/<int:pk>/editar/', views.AulaUpdateView.as_view(), name='aula_update'),
    path('aulas/<int:pk>/eliminar/', views.AulaDeleteView.as_view(), name='aula_delete'),
    path('grupos/', views.GrupoListView.as_view(), name='grupo_list'),
    path('grupos/nuevo/', views.GrupoCreateView.as_view(), name='grupo_create'),
    path('grupos/<int:pk>/editar/', views.GrupoUpdateView.as_view(), name='grupo_update'),
    path('grupos/<int:pk>/eliminar/', views.GrupoDeleteView.as_view(), name='grupo_delete'),
    path('', views.inicio, name='inicio'),
    path('profesores/', views.ProfesorListView.as_view(), name='profesor_list'),
    path('profesores/nuevo/', views.ProfesorCreateView.as_view(), name='profesor_create'),
    path('profesores/<int:pk>/editar/', views.ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/<int:pk>/eliminar/', views.ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiantes/nuevo/', views.EstudianteCreateView.as_view(), name='estudiante_create'),
    path('estudiantes/<int:pk>/editar/', views.EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('estudiantes/<int:pk>/eliminar/', views.EstudianteDeleteView.as_view(), name='estudiante_delete'),
    path('materias/', views.MateriaListView.as_view(), name='materia_list'),
    path('materias/nuevo/', views.MateriaCreateView.as_view(), name='materia_create'),
    path('materias/<int:pk>/editar/', views.MateriaUpdateView.as_view(), name='materia_update'),
    path('materias/<int:pk>/eliminar/', views.MateriaDeleteView.as_view(), name='materia_delete'),


    path('grupos/<int:grupo_id>/calificaciones/', views.capturar_calificaciones, name='capturar_calificaciones'),
]
