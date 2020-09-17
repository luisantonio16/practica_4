#Crear una clase Aritmetica, que contega todas las operaciones aritmetica

class Aritmetica:
    def __init__(self):
       pass

    def Suma(self,n1,n2):
       self.sumar = n1 + n2
       print(" la suma es: "+ str(self.sumar))

    def Resta(self,n1,n2):
       self.restar = n1 - n2
       print(" la Resta es: "+ str(self.restar))

    def Multiplicacion(self,n1,n2):
       self.multiplicar = n1 * n2
       print(" la Multiplicacion es: "+ str(self.multiplicar))

    def Division(self,n1,n2):
       self.dividir = n1 / n2
       print(" la Division es: "+ str(self.dividir))


calcular = Aritmetica()
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
calcular.Suma(num1, num2)
calcular.Multiplicacion(num1,num2)





    
