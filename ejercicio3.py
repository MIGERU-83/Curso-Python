
class Numero:
    def __init__(self, numero):
        self.numero = numero
        
    def evaluarNumero(self):
        if self.numero & 1:
            print("El número ingresado es impar")
            if self.numero == 7:
                print("\nEl número ingresado es impar y es un comodin")
        else:        
            print("El número ingresado es par")
            if self.numero == 10:
                print("\nEl número ingresado es par y es el 10")

    def sumar(self, numeroasumar):
        return self.numero + numeroasumar                                 
                
     
if __name__ == "__main__":
   numeroaevaluar = Numero(int(input("Ingrese un número: \n")))
   numeroaevaluar.evaluarNumero()
   sumarealizada = numeroaevaluar.sumar(4)
   print("\nLa suma realizada es: ", sumarealizada)