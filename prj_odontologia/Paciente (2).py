from statistics import variance
from tkinter import Variable
from Persona import Persona
from Turno import Turno



class Paciente(Persona):
    def __init__(self,nombre,apellido,edad,dni,obrasocial): 
        self.obrasocial=obrasocial
        self.turno=None
        Persona.__init__(self,nombre,apellido,edad,dni)
    
    def AgregarTurno(self,dia,mes,año,hora,minutos):
        if (self.turno==None):
            self.turno=Turno(dia,mes,año,hora,minutos,0)   #los paréntesis ¿? preguntar!

    def EliminarTurno(self):
        self.turno=None

    def ImprimirTurno(self):
        if(self.turno == None):
            print("Este paciente no tiene un turno.")
        else:
            print(self.turno.GetFechaYHora())

    def GetObraSocial(self):
        return self.obrasocial
        
