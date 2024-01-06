# Mostrar la tabla de multiplicar de N
num = int()
cont = int()
print("INGRESE NUMERO: ", end="")
num = int(input())
for cont in range(1,13):
	print(num," x ",cont," = ",(num*cont))

