# Mostrar la cantidad de numeros pares e impares
num = int()
x = int()
sumap = int()
sumai = int()
sumap = 0
sumai = 0
print("INGRESE UN NUMERO : ", end="")
num = int(input())
for x in range(1,num+1):
	if (x%2)==0:
		sumap = sumap+x
	elif (x%2)==1:
		sumai = sumai+x
print("Suma de pares    : ",sumap)
print("Suma de impares  : ",sumai)

