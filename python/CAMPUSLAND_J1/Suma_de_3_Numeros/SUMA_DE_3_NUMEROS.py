#1. Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima
#La sumatoria de los tres números.
import os
N1=0
N2=0
N3=0
result=0
print(f"\n=======================")


print(f"\n BIENBENIDOS ")

print(f"\n======================")

print("Ingrese un Numero ")
N1=int(input())
print("Ingrese un Numero ")
N2=int(input())
print("Ingrese un Numero ")
N3=int(input())
os.system ("cls")
if (N1>=1) and (N2>=1) and (N3>=1) :
    result=N1+N2+N3
    print("El resultado es : ",result )
else :

    print ("\nSolo Numeros positivos y enteros")