"""Crear una clase llamada estudiante que contega un campo promedio, el cual solo pueda ser acedido mediante
un metodo. el valor del promedio no puede estar por encima de 100 que es la nota maxima"""

class Estudiantes:
     promedio = 0

     def nota(self,promen):
         self.promedio = promen
         if promen >=100:
             print("El limite de tu Promedio es 100")
         else:
             print(" Tu promedio es: "+ str(promen))
         return self.promedio    


resultado = Estudiantes()
resultado.nota(120)