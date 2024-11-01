import os
from sympy import *
import numpy as np

def ingresar_datos(matrizA, size):
    for i in range(size):
        for j in range(size+1):
            matrizA[i][j] = float(input(f"Ingresa el valor de la posición {i+1} , {j+1}: "))

def reordenar_filas(matrizA, size):
    cambio = False
    for fila in range(size):
        if (matrizA[fila][fila] == 0):
            iteracion = 0
            while (cambio == False) and (iteracion < size):
                if (fila != iteracion):
                    if(matrizA[iteracion][fila] != 0):
                        matrizA[[fila, iteracion]] = matrizA[[iteracion, fila]]
                        cambio = True
                iteracion = iteracion + 1
        cambio = False
    print(matrizA)

def reordenar_columnas(matrizA, size):

    for fila in range(size):
        suma = 0
        for columna in range(size):
            if columna != fila:
                suma += np.abs(matrizA[fila][columna])

        if np.abs(matrizA[fila][fila]) < suma:
            # Busca la columna con el mayor valor absoluto fuera de la diagonal
            max_col = -1
            max_val = -1
            for iteracion in range(size-1):
                if iteracion != fila:
                    if np.abs(matrizA[fila][iteracion]) > max_val:
                        max_val = np.abs(matrizA[fila][iteracion])
                        max_col = iteracion

            if max_col != -1:
                # Intercambia columnas para hacer la matriz diagonalmente dominante
                matrizA[:, [fila, max_col]] = matrizA[:, [max_col, fila]]


    print(matrizA)

def Dominante(matrizA, size):
    for fila in range(size):
        suma_fuera_diagonal = 0
        for columna in range(size):
            if columna != fila:
                suma_fuera_diagonal += np.abs(matrizA[fila][columna])
        if np.abs(matrizA[fila][fila]) < suma_fuera_diagonal:
            return False
    return True




def Gaussiana(matrizA, size):

    reordenar_filas(matrizA, size)
    flag = True

    diagonal = np.diagonal(matrizA)

    for fila in range(size):
        if (diagonal[fila] == 0):
            flag = False

    if flag:
        for k in range(size):
            for i in range(k + 1, size):
                if matrizA[k][k] != 0:  # Evitar división por 0
                    factor = matrizA[i][k] / matrizA[k][k]
                    for j in range(k, size + 1):
                        matrizA[i][j] = matrizA[i][j] - (factor * matrizA[k][j])
                else:
                    print(f"División por 0 evitada en la fila {k + 1}")
                    return

        terminos_independientes = matrizA[:, -1]

        for i in range(size - 1, -1, -1):
            suma = 0
            for j in range(i + 1, size):
                suma += matrizA[i][j] * terminos_independientes[j]
            if not np.isclose(matrizA[i][i], 0):  # Evitar división por 0
                terminos_independientes[i] = (matrizA[i][-1] - suma) / matrizA[i][i]
            else:
                print(f"División por 0 evitada en la fila {i + 1}")
                return

        print("Soluciones:")
        for i in range(len(terminos_independientes)):
            print(f"X{i+1} = {terminos_independientes[i]}")
    else:
        print("No se pudo evitar un 0 en la diagonal. Modifica el sistema para que no haya un 0 en la diagonal")



def Gauss_Seidel(matrizA, size):
    matrizB = np.zeros(size, dtype=float)
    valuesX = np.zeros(size, dtype=float)
    PastValues = np.zeros(size, dtype=float)
    Errors = np.full(size, 100, dtype=float)
    iteracion = 0

    matrizB = matrizA[:, -1]

    Error_Deseado = float(input("Ingresa el error deseado: "))

    # Verificación de dominancia diagonal
    reordenar_columnas(matrizA, size)
    reordenar_filas(matrizA, size)

    dominante = Dominante(matrizA, size)
    if dominante:

        diagonal = np.diagonal(matrizA)

        while np.any(np.abs(Errors) > Error_Deseado):

            iteracion += 1
            PastValues[:] = valuesX

            for i in range(size):
                suma = 0
                for j in range(size):
                    if j != i:
                        suma += matrizA[i, j] * valuesX[j]

                if diagonal[i] != 0:  # Verificar que no se divida por 0
                    valuesX[i] = (matrizB[i] - suma) / diagonal[i]
                else:
                    print(f"División por 0 evitada en la fila {i + 1}")
                    return  # O manejar de otra manera

            for i in range(size):
                if valuesX[i] != 0:  # Evitar división por 0 al calcular el error
                    Errors[i] = np.abs((valuesX[i] - PastValues[i]) / valuesX[i]) * 100
                else:
                    Errors[i] = np.inf  # Manejar el error adecuadamente


        for i in range(size):
            print(f"El valor de X{i + 1} es: {valuesX[i]}")
    else:
        print("El sistema no es diagonalmente dominante")

def Gauss_Jordan(matrizA, size):

    reordenar_filas(matrizA, size)

    for i in range(size):
        # Verificar si el pivote es cero para evitar errores
        if matrizA[i, i] == 0:
            raise ValueError(f"El pivote en la fila {i} es cero. No se puede continuar con la eliminación Gauss-Jordan.")

        # Normalizar la fila actual, incluyendo la última columna
        matrizA[i] = matrizA[i] / matrizA[i, i]

        # Eliminar las otras entradas en la columna i
        for j in range(size):
            if i != j:
                factor = matrizA[j, i]
                matrizA[j] = matrizA[j] - factor * matrizA[i]

    # Extraer las soluciones de la última columna
    soluciones = matrizA[:, -1]

    # Imprimir los resultados de las incógnitas
    print("Los valores de las incógnitas son:")
    for i in range(size):
        print(f"x{i+1} = {soluciones[i]}")

def leer_expresion():
    x = symbols("x")
    #Se lee la función a analizar
    try:
        string_expression = input("Ingresa la expresion: ")
        expression = sympify(string_expression)
        print(expression)
    except Exception as e:
        print("Error al analizar la expresion: ", e)

    return expression

def Newton_Raphson():

    x = symbols("x")

    expression = leer_expresion()

    #Se obtiene la derivada de la expresión
    derivate = diff(expression, x)
    segunda_derivada = diff(expression, x, 2)

    error_deseado = int(input("Ingresa el error deseado en porcentaje: "))
    error = 100
    raiz_n = float(input("Ingresa el valor inicial: "))
    raiz_x = 0.0 #Este es el valor de x_n+1
    iteraciones = 0
    max_iteraciones = 1000

    numerador_criterio = expression.subs(x, raiz_n) * segunda_derivada.subs(x, raiz_n)
    denominador_criterio = (derivate.subs(x, raiz_n))**2

    criterio = abs(numerador_criterio/denominador_criterio)

    if criterio < 1:
        while (error > error_deseado):
            #Se obtiene el valor 
            numerador = (expression.subs(x, raiz_n))
            denominador = derivate.subs(x, raiz_n)

            if denominador == 0:
                print("El denominador vale cero. No se puede continuar con el método")
                return

            raiz_x = raiz_n - (numerador / denominador) 
            error = abs((raiz_x - raiz_n)/raiz_x) * 100
            raiz_n = raiz_x

        print(f"Una buena aproximacion a la solucion con un porcentaje de error {error_deseado} es {raiz_x} ")
    else:
        print("La función no converge en el punto dado")

def Newton_Raphson_Mejorado():
    x = symbols("x")

    expresion = leer_expresion()

    #Se obtienen las derivadas
    primera_derivada = diff(expresion, x)
    segunda_derivada = diff(expresion, x, 2)

    error = 100.0
    error_deseado = float(input("Ingresa el error deseado: "))
    raiz_n = float(input("Ingresa el valor inicial del x: "))
    raiz_x = 0
    iteraciones = 0
    max_iteraciones = 1000

    while (error > error_deseado) and (iteraciones <= max_iteraciones):
        numerador = expresion.subs(x, raiz_n)*primera_derivada.subs(x, raiz_n)
        denominador = (primera_derivada.subs(x, raiz_n))**2 - (expresion.subs(x, raiz_n)*(segunda_derivada.subs(x, raiz_n)))

        if denominador == 0:
            print("El denominador vale cero, no se puede continuar con el método")
            return

        raiz_x = raiz_n - (numerador/denominador)
        error = abs((raiz_x - raiz_n) / raiz_x) * 100
        raiz_n = raiz_x

        if iteraciones == max_iteraciones:
            print("Se ha alcanzo el limite de iteraciones")
    print("Una buena aproximacion con un error menor al ", error, "es", raiz_x)

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
        print("2.- Interpolación lineal")
        print("3.- Eliminación Gaussiana")
        print("4.- Gauss-Jordan")
        print("5.- Gauss-Seidel")
        print("6.- Interpolación Newton-Raphson")
        print("7.- Interpolación Newton-Raphson Mejorado")
        print("8.- Salir")
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
