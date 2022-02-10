from django.db import models
from django.utils.datetime_safe import datetime


class Theatre(models.Model):
    theatre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)


class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot_date = models.DateField(max_length=20, unique=False)
    start_time = models.TimeField(default=datetime.now, blank=False)
    end_time = models.TimeField(default=datetime.now, blank=False)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)


