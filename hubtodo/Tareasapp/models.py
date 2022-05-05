from pyclbr import Class
from django.db import models

# Create your models here.

class Tareas(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    dead_line = models.DateField()
    description = models.CharField(max_length=50)
    isCompleted = models.BooleanField()
    priority_id = models.IntegerField()
    id_usuario = models.IntegerField()