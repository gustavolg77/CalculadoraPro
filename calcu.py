import math
#menu principal de la calculadora



#funcion suma
def suma(a, b):
    return a + b


#funcion resta
def resta(a, b):
    return a - b



#funcion multiplicacion

def multiplicar(a, b):
    return a * b

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
