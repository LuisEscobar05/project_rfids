from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from Alumno.models import Alumno


class Asistencia(models.Model):
    date = models.DateTimeField(default= timezone.now)
    id_alumno = models.ForeignKey(Alumno, on_delete = models.SET(-1))

    class Meta:
        db_table = 'asistencia'

    def __str__(self):
        return self.id
        