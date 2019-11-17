from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Rfid(models.Model):
    date = models.DateTimeField(default= timezone.now)
    number_rfid = models.CharField(max_length=30, null=False)
    status = models.BooleanField(null=False)

    class Meta:
        db_table = 'Rfid'

    def __str__(self):
        return self.id
        