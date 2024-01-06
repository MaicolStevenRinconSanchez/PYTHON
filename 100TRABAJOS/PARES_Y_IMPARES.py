print ("INGRESE NUMERO")
# Estructura REPETITIVA PARA
# Mostrar  cantidad de numeros PARES e IMPARES 
# Declarar Variable.
cont = int()
num = int()
pars = int()
impars = int()
pars = 0
impars = 0
print()
for cont in range(1,11):
	print("NUMERO ",cont," : ", end="")
	num = int(input())
	if (num%2)==0:
		pars = pars+1
	else:
		impars = impars+1
print("CANTIDAD DE PARES  : ",pars)
print("CANTIDAD DE IMPARES : ",impars)

