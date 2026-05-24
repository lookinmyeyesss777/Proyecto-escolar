from django.db import models

# ==========================================
# 1. CATÁLOGOS BASE (Sin dependencias)
# ==========================================

class Carrera(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Carrera")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"


class PeriodoSemestral(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Periodo (Ej: Enero-Junio 2026)")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Periodo Semestral"
        verbose_name_plural = "Periodos Semestrales"


class Aula(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre/Número de Aula")
    capacidad = models.IntegerField(verbose_name="Capacidad de Alumnos")
    ubicacion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Ubicación/Edificio")

    def __str__(self):
        return f"{self.nombre} ({self.ubicacion})"

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"


class Horario(models.Model):
    dias = models.CharField(max_length=100, verbose_name="Días (Ej: Lunes y Miércoles)")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    hora_fin = models.TimeField(verbose_name="Hora de Fin")

    def __str__(self):
        return f"{self.dias} [{self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}]"

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"


# ==========================================
# 2. ENTIDADES CON LLAVES FORÁNEAS BÁSICAS
# ==========================================

class Materia(models.Model):
    clave = models.CharField(max_length=20, unique=True, verbose_name="Clave de la Materia")
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Materia")
    creditos = models.IntegerField(verbose_name="Créditos")
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name="Carrera Asociada")

    def __str__(self):
        return f"{self.clave} - {self.nombre}"

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


class Estudiante(models.Model):
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    nombre = models.CharField(max_length=100, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name="Carrera")

    # NOTA: Aquí ya no va el campo 'grupo', se maneja de forma inversa en la clase Grupo.

    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellidos}"

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


# ==========================================
# 3. EL NÚCLEO TRANSACCIONAL (Módulo de Grupos)
# ==========================================

class Grupo(models.Model):
    nombre = models.CharField(max_length=10, verbose_name="Nombre del Grupo (Ej: 8A)")
    
    # Llaves foráneas obligatorias según la rúbrica
    profesor = models.ForeignKey(Profesor, on_delete=models.RESTRICT, verbose_name="Profesor")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia")
    aula = models.ForeignKey(Aula, on_delete=models.RESTRICT, verbose_name="Aula")
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.CASCADE, verbose_name="Periodo Semestral")
    horario = models.ForeignKey(Horario, on_delete=models.RESTRICT, verbose_name="Horario")
    
    # Relación Muchos a Muchos para los alumnos inscritos
    estudiantes = models.ManyToManyField(Estudiante, blank=True, related_name='grupos_inscritos', verbose_name="Estudiantes Inscritos")

    def __str__(self):
        return f"Grupo {self.nombre} - {self.materia.nombre} ({self.periodo.nombre})"

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"


# ==========================================
# 4. MÓDULO DE CALIFICACIONES
# ==========================================

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo")
    
    # Mapeo explícito solicitado por la rúbrica
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia")
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.CASCADE, verbose_name="Periodo")
    
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Calificación Final")

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
        # Impide que se duplique la calificación de un alumno en un mismo grupo
        unique_together = ('estudiante', 'grupo')

    def __str__(self):
        return f"{self.estudiante.matricula} - {self.materia.nombre}: {self.valor}"