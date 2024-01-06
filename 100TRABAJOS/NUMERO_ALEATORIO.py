import random
# Encotrar un numero aleatroio de 1 al 20
num = int()
i = int()
numa = int()
sw = int()
sw = 0
numa = random.randint(1, 20)
for i in range(-1,4):
	print("ENCUENTRE EL NUMERO 	[1 - 20] : ")
	num = int(input())
	if (num==numa):
		print("NUMERO ENCONTRADO")
		sw = 1
		i = 3
	else:
		if (num>numa):
			print("INGRESE UN NUMERO MENOR")
		else:
			print("INGRESE UN NUMERO MAYOR")
	print(" ")
if (sw==0):
	print("EL NUMERO A ENCONTRAR ERA : ",numa)

