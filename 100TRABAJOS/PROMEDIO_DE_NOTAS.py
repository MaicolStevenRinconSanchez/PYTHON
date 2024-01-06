# Mostrar el promedio de varias notas
cont = int()
n = int()
nota = int()
suma = int()
suma = 0
print("INGRESE LA CANTIDAD DE NOTAS : ")
n = int(input())
for cont in range(1,n+1):
	print("NOTA ",cont," : ", end="")
	nota = int(input())
	suma = suma+nota
print("PROMEDIO : ",(suma/n))

