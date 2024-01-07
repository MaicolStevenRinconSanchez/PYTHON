import os 
Nombre = str ()
edad = int ()
altura =float ()
peso = float ()
IMC=float ()
print ("\n Centro de Salud")
print ("Ingrese su Nombre")
nombre =str(input() )
print ("Ingrese su Edad")
edad = int(input())
print ("Ingrese su Altura")
altura = float(input() )
print ("Ingrese su Peso")
peso = float(input() )

IMC=peso/(altura*altura)

os.system("cls")
if (IMC>= 18.5) and (IMC<=24.9) :
    
    print ("\nEl indice de masa corporal del estudiante",nombre,"con la edad de  ",edad, "y el IMC :",IMC )
    print ("\n Su peso es  NORMAL")
elif (IMC>= 25) and (IMC<=29.9)  :
    print ("\nEl indice de masa corporal del estudiante",nombre,"con la edad de  ",edad, "y el IMC :",IMC )
    print ("\n Su peso es  SOBREPESO")
elif (IMC>= 30) and (IMC <=34.9) :
    print ("\nEl indice de masa corporal del estudiante",nombre,"con la edad de  ",edad, "y el IMC :",IMC )
    print ("\n Su peso es  OBESIDAD I")
elif (IMC>= 35) and (IMC<=39.9) :
    print ("\nEl indice de masa corporal del estudiante",nombre,"con la edad de  ",edad, "y el IMC :",IMC )
    print ("\n Su peso es  OBESIDAD II")
elif IMC>= 40 :
    print ("\nEl indice de masa corporal del estudiante",nombre,"con la edad de  ",edad, "y el IMC :",IMC )
    print ("\n Su peso es  OBESIDAD III")
else :
    print ("Positivo para desnutrido")
