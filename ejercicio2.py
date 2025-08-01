def evaluar_numero(numero):
    
    if numero == 10:
        print("El número ingresado es par y es el 10")
    elif numero == 7:
        print("El número ingresado es impar y es un comodín")
    
    elif numero % 2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")


def main():
    while True:
        try:
            print("\n=== Evaluador de Números ===")
            num = input("Ingrese un número (o escriba 'exit' para salir): ")
            
            if num.lower() == 'exit':
                print("¡Hasta luego!")
                break
                
            evaluar_numero(int(num)) # pyright: ignore[reportUnusedVariable]
        except ValueError:
            print(f"Ingresa un numero valido:")

if __name__ == "__main__":
    main()