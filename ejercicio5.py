#ejercicio 5 de Herencia


class Carro:
     def __init__(self,galones,piston):
         self.cantidad_combustible = galones
         self.numero_pistones = piston
         self.arrancar = False

     def cantidad_galones(self):
         self.cantidad_combustible -= 1
        

     def enceder(self):
         if self.cantidad_combustible > 0 and self.arrancar == False:
             print("El super Auto esta encendido!!")
             self.arrancar = True
             self.cantidad_galones()



class Lamborghini(Carro):
         def arrancar(self):
              print("La lamborghini URUS, va 260 km * hora")
 


auto = Carro(50,12)
auto.enceder()
auto1 = Lamborghini()
auto1.arrancar()






    