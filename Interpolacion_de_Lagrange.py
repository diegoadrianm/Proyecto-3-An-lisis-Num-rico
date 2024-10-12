import os
from sympy import *

def interpolacion():
    x = symbols('x')
    try:
        string_expression = input("Ingresa la expresion: ")
        expression = sympify(string_expression)
    except Exception as e:
        print("Error al analizar la expresion: ", e)

    while True:
        try:
            y = float(input("Ingresa el valor de x a evaluar: "))
        except ValueError:
            print("Error al ingresar el valor de x")
            continue
        break
    
    while True:
        try:
            x0 = float(input("Ingresa el valor de x1: "))
        except ValueError:
            print("Error al ingresar el valor de x1")
            continue
        break

    while True:
        try:
            x1 = float(input("Ingresa el valor de x2: "))
        except ValueError:
            print("Error al ingresar el valor de x2")
            continue
        break

    fx0 = expression.subs(x, x0)
    fx1 = expression.subs(x, x1)

    fx = fx0 + ((fx1 - fx0*(y - x0))/(x1 - x0))
    fx_rounded = round(fx, 3)

    print(f"Una buena aproximación es: {fx_rounded}")

def Lagrange():
    pares = {}
    suma = 0
    num_pares = int(input("Ingresa la cantidad de pares ordenados: "))
    for i in range(num_pares):
        x = float(input(f"ingresa el valor de x{i} "))
        y = float(input(f"ingresa el valor de y{i} "))
        pares[i] = [x, y]

    print(pares)
    valor = float(input("Ingresa el valor a interpolar: "))

    for i in range(num_pares):
        numerador = 1
        denominador = 1
        for j in range(num_pares):
            if j != i:
                numerador *= valor - pares[j][0]
                denominador *= pares[i][0] - pares[j][0]
        suma += pares[i][1] * (numerador/denominador)

    print(f"El valor de la y para la X dada es: {suma}")


def menu():
    flag = True
    while flag:
        os.system('cls')
        print("1.- Interpolación de Lagrange")
        print("7.- Salir")
        opcion = int(input("Ingrese la opción deseada "))

        if opcion == 1:
            Lagrange()
        elif opcion == 2:
            interpolacion()

        resp = input("¿Reiniciar? (S/N): ")
        if resp in ('N', 'n'):
            flag = False
        os.system('cls')


menu()
