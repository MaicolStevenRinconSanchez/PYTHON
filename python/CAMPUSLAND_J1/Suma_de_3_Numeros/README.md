Sumatoria de Tres Números Enteros Positivos
Este programa simple en Python permite al usuario ingresar tres números enteros positivos y calcula la sumatoria de los mismos. Además,
incluye una validación para asegurarse de que los números ingresados sean positivos.

1.Ingreso de Números:
El programa solicita al usuario ingresar tres números enteros positivos.

import os
N1 = 0
N2 = 0
N3 = 0
result = 0
print(f"\n=======================")
print(f"\n BIENVENIDOS ")
print(f"\n======================")
print("Ingrese un Numero ")
N1 = int(input())
print("Ingrese un Numero ")
N2 = int(input())
print("Ingrese un Numero ")
N3 = int(input())
os.system("cls")

2.Cálculo de la Sumatoria:
El programa verifica que los números ingresados sean positivos antes de calcular la sumatoria.

if (N1 >= 1) and (N2 >= 1) and (N3 >= 1):
    result = N1 + N2 + N3
    print("El resultado es : ", result)
else:
    print("\nSolo se permiten números positivos y enteros.")

