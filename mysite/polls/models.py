from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

class empleado(models.Model) : 
    id = models.SmallIntegerField(primary_key= True)
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100) 
    fecha_inicio = models.DateField()
    dias_trabajo = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    horario_in = models.DateTimeField()
    horario_out = models.DateTimeField()

class jornada(models.Model) : 
    id = models.SmallIntegerField(primary_key= True) 
    empleado.id = models.SmallIntegerField(primary_key= True) 
    fecha = models.DateField()
    tipo_marc = models.CharField(max_length=100) 


# Create your models here.
