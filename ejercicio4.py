#ejercicio de Herencia.


class Personaje:
      def __init__(self):
           pass
          
      def Moverarriba(self):
           print("brinco hacia Arriba y encotro una Flor de Fuego")

      def Moverabajo(self):
           print("se deslizo hacia abajo en el tubo y encotro a un caballito Amarillo")

      def Moverizquierda(self):
           print(" va hacia la izquierda para salvar a la princesa")

      def Moverderecha(self):
           print(" se dirige para la derecha, para que Boswer no lo atrape")   


class Mario(Personaje):
      def jugar(self):
              self.nombre = "Mario" 
              print(""+str(self.nombre))


class koopa(Personaje):
     def jugar1(self):
         self.nombre = "BOSWER" 
         print("" +str(self.nombre)+ " Quiere quedarse con la princesa peach")
         

         


jugador = Mario()
jugador.jugar()
jugador.Moverabajo()
jugador.jugar()
jugador.Moverarriba()
jugador.jugar()
jugador.Moverderecha()
print("-----------------")
jugador1= koopa()
jugador1.jugar1()
jugador.jugar()
jugador.Moverizquierda()

           


