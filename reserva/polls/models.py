from django.db import models

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Hotel(models.Model) : 
    id = models.SmallIntegerField(primary_key= True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class reserva(models.Model) :
    id = models.SmallIntegerField(primary_key= True)
    fe_in = models.DateField()
    fe_sal = models.DateField()
    nhuesped = models.CharField(max_length = 10)
    habtip = models.CharField(max_length = 100) 
    precio = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 100)


    

# Create your models here.
