#!/usr/bin/python3

def multiplicar():
    tabla1 = range(1,11)
    tabla2 = range(1,11)

    for num1 in tabla1:
        print("Tabla del ", num1)
        print("----------------")
        for num2 in tabla2:
            resultado = num1 * num2
            print(num1, " por ", num2, " es ", resultado)
        print('\n')

multiplicar()
