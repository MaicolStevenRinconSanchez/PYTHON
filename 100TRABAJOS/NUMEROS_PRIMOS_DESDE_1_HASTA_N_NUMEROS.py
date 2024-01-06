# Mostrar la serie de numeros primos.
num = int()
cont = int()
divi = int()
divisible = int()
divisible = 0
print("INGRESE UN VALOR : ", end="")
num = int(input())
for cont in range(2,num+1):
	for divi in range(1,cont+1):
		if ((cont%divi)==0):
			divisible = divisible+1
	if (divisible==2):
		print(cont," ", end="")
	divisible = 0
print("")

