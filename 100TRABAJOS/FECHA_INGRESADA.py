# Declaracion de variables
dias = int()
a = int()
m = int()
d = int()
print("INGRESE LA CANTIDAD DE DIAS : ", end="")
dias = int(input())
a = int(dias/365)
m = int((dias-(a*365))/30)
d = int(dias-((a*365)*(m*30)))
print("Año : ",a)
print("Mes : ",m)
print("Dia : ",d)

