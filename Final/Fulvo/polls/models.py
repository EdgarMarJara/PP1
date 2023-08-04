from django.db import models

# Create your models here.
class Canchas (models.Model): 
    Tipo = models.CharField(max_length=100)
    Nombre = models.CharField(max_length= 100)
    Ciudad = models.CharField(max_length=100)
    Departamento = models.CharField(max_length=100)
    Hora_abre = models.TimeField()
    Hora_cerra = models.TimeField()
    #def __str__(self):
    #    return self.Nombre
    
class Reserva (models.Model): 
    ID_cancha = models.ForeignKey(Canchas, on_delete=models.PROTECT, db_column='ID_cancha', blank=True, null=True) 
    Hora_Inicio = models.TimeField()
    Hora_Fin = models.TimeField() 
    #def __str__(self):
    #    return self.ID_cancha



class Gestion (models.Model): 
    ID_Reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT, db_column='ID_Reserva', blank=True, null=True) 
    Estado = models.CharField(max_length= 20)
    Recomendacion = models.CharField(max_length= 200)
    
    #def __str__(self):
    #    return self.ID_Reserva




