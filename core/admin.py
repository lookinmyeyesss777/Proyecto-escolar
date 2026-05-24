from django.contrib import admin

from .models import (
	Profesor, Estudiante, Materia, Carrera, Aula, Grupo, Horario, Calificacion, PeriodoSemestral
)

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Carrera)
admin.site.register(Aula)
admin.site.register(Grupo)
admin.site.register(Horario)
admin.site.register(Calificacion)
admin.site.register(PeriodoSemestral)
