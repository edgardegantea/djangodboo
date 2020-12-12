from django.db import models
from datetime import *


# Create your models here.
class Evidencia(models.Model):
    name = models.CharField(verbose_name='Evidencia', max_length=255)
    files = models.FileField(upload_to='evidencias/%Y/%m/%d', null=True, blank=True)
    description = models.CharField(verbose_name='Descripción', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Evidencia'
        verbose_name_plural = 'Evidencias'
        ordering = ['id']


class Acuerdo(models.Model):
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=10, verbose_name='Prefijo', default='A.IINF')
    number = models.CharField(max_length=3, verbose_name='Número')
    TIPO_SESION = {('SO', 'Sesión Ordinaria'), ('SE', 'Sesión Extraordinaria')}
    session = models.CharField(choices=TIPO_SESION, default='SO', max_length=20, verbose_name='Tipo de sesión')
    date = models.DateField(auto_now_add=True, verbose_name='Fecha')
    name = models.CharField(verbose_name='Acuerdo', max_length=255)
    description = models.TextField(verbose_name='Descripción del acuerdo')
    ESTADO_ACUERDO = [('En proceso', 'En proceso'), ('Concluido', 'Concluido'), ('Iniciado', 'Iniciado')]
    status = models.CharField(choices=ESTADO_ACUERDO, default='Iniciado', verbose_name='Estado', max_length=30)

    def __str__(self):
        return "{0}-{1}-{2}/{3}".format(self.prefix, self.session, self.date, self.name)

    class Meta:
        verbose_name = 'Acuerdo'
        verbose_name_plural = 'Acuerdos'
        ordering = ['id']


class Asistentes(models.Model):
    name = models.CharField(max_length=100, verbose_name='Asistente')
    NOMBRAMIENTO = [('Medio tiempo', 'Medio tiempo'), ('Tres cuartos de tiempo', 'Tres cuartos de tiempo'), ('Tiempo completo', 'Tiempo completo')]
    appointment = models.CharField(choices=NOMBRAMIENTO, verbose_name='Nombramiento', default='Medio tiempo', max_length=50)
    ACADEMIC_BODY = [('Innovación disruptiva', 'Innovación disruptiva'), ('Mejora contínua', 'Mejora contínua')]
    academicbody = models.CharField(choices=ACADEMIC_BODY, verbose_name='Cuerpo académico', default='', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asistente'
        verbose_name_plural = 'Asistentes'
        ordering = ['appointment']


class Acta(models.Model):
    asistentes = models.ManyToManyField(Asistentes)
    number = models.CharField(verbose_name='Número de acta', max_length=3)
    TIPO = [('SO', 'Sesión Ordinaria'), ('SE', 'Sesión Extraordinaria')]
    type = models.CharField(choices=TIPO, default='SO', max_length=20, verbose_name='Tipo de sesión')
    # type = models.CharField(max_length=30, verbose_name='Tipo de sesión')
    description = models.TextField(verbose_name='Descripción')
    date = models.DateField(auto_now_add=True, verbose_name='Fecha')
    ESTAD0 = [('En redacción', 'En redacción'), ('En revisión', 'En revisión'), ('Aprobada', 'Aprobada')]
    status = models.CharField(choices=ESTAD0, default='En redacción', max_length=30)
    acuerdos = models.ManyToManyField(Acuerdo)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Acta'
        verbose_name_plural = 'Actas'
        ordering = ['date']



