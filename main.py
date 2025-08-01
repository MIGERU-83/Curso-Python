#Funciones en Python
def saludar(nombre):
    print(f"Hola {nombre}") 
    print("¿Cómo estás?")
    
def main():   
    nombre = input("ingrese un nombre:  ") 
    saludar(nombre)
    
if __name__ == "__main__":
    main()
print("Nueva línea")
print("Fin del programa")