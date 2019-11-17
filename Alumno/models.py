from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from Rfid.models import Rfid


class Alumno(models.Model):
    name = models.CharField(max_length=50, null=False)
    matricula = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=60, null=False)
    id_rfid = models.ForeignKey(Rfid, on_delete = models.SET(-1))

    class Meta:
        db_table = 'Alumno'

    def __str__(self):
        return self.id
        