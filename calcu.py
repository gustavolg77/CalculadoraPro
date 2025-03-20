import math

#funcion suma
def suma(a, b):
    return a + b


#funcion resta
def resta(a, b):
    return a - b



#funcion multiplicacion



#funcion division
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    else: 
        return a / b


#funcion de potencia
def power(a, b):
    return a ** b

#funcion de raiz cuadrada


#funcion de raiz cuadrada
def raiz_cuadrada(numero):
    
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(numero)





#funcion de modulo (resto de la division)
def modulo(a, b):
    if b==0:
       return "ERROR"
    return a % b



#funcion de factorial
def factorial(num):
    aux = num
    res = 1
    if aux==0:
        return res
    else:
        for i in range(aux):
            res = res*num
            num = num-1
    return res


#funcion de logaritmo
#MENU INTERACTIVO DE LA CALCULADORA PRO

def menu():
    while True: 
        print("\n ****CALCULADORA PRO****")
        print("\n 1. Suma")
        print("\n 2. Resta")
        print("\n 3. Multiplicacion ")
        print("\n 4. Division ")
        print("\n 5. Potencia ")
        print("\n 6. Raiz cuadrada")
        print("\n 7. Modulo ")
        print("\n 8. Factorial")
        #print("\n 9.Logaritmo")
        print("\n 9. Salir ")

        opcion = input("Elige una opcion:  ")

        if opcion == "9":
            print ("Saliendo de la CALCULADORA PRO! ")
            break
        if opcion in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))

            if opcion == "1":
                print("Resultado:", suma(a, b))
            elif opcion == "2":
                print("Resultado:", resta(a, b))
            elif opcion == "3":
                print("Resultado:", multiplicacion(a, b))
            elif opcion == "4":
                print("Resultado:", dividir(a, b))
            #elif opcion == "5":
             #   print("Resultado:", potencia(a, b))
            elif opcion == "7":
                print("Resultado:", modulo(a, b))
# aqui los parametros que se recibe son distintos

        elif opcion == "6":
            numero = float(input("Ingresa un numero: "))
            print("Resultado:", raiz_cuadrada(numero))

        elif opcion == "8":
            num = int(input("Ingresa un número entero: "))
            print("Resultado:", factorial(num))

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()