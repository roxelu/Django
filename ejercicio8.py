"""
Nombre: Roxana Luque
Comisión: 23266

Ejercicio 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7.
"""
from ejercicio7 import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
    