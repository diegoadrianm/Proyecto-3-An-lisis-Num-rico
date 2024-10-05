import os


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

        resp = input("¿Reiniciar? (S/N): ")
        if resp in ('N', 'n'):
            flag = False
        os.system('cls')


menu()
