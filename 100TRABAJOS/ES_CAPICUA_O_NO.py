# Mostrar si es un numero capicua
i = int()
num = str()
tem = str()
tem = " "
print("INGRESE NUMERO : ", end="")
num = input()
for i in range(len(num)-1,-1,-1):
	tem = tem+num[i-1:i]
print(" ")
print("NUMERO INGRESADO : ",num)
print("NUMERO CAMBIADO  : ",tem)
if (num==tem):
	print("SI ES UN NUMERO CAPICUA")
else:
	print("NO ES UN NUMERO CAPICUA")

