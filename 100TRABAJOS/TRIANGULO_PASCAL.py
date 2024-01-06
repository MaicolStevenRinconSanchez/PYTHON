n = int()
m = int()
e = int()
izq = int()
der = int()
val = int()
espacios = str()
# Matriz de 20x20
m = [[int() for ind0 in range(20)] for ind1 in range(20)]
# ingreso de datos
print("MOSTRAR EL TRIANGULO DE PASCAL")
print("INGRESE DIMENSION  [MENOS O IGUAL A 20]: ", end="")
n = int(input())
# Procceso :Crear el traingulo en la matriz 
for izq in range(1,n+1):
	for der in range(2,n+1):
		m[izq-1][der-1] = 0
# Coloca el valor de 1 en los extremos 
for izq in range(1,n+1):
	m[izq-1][0] = 1
for der in range(1,n+1):
	m[der-1][der-1] = 1
for izq in range(3,n+1):
	for der in range(2,izq+1):
		m[izq-1][der-1] = m[izq-2][der-1]+m[izq-2][der-2]
# Proceso : Mostrar el triangulo
for izq in range(1,n+1):
	espacios = " "
	for e in range(1,izq-n+1):
		espacios = espacios+" "
	print(espacios, end="")
	for der in range(1,izq+1):
		val = m[izq-1][der-1]
		if (val!=0):
			print(val," ", end="")
	print(" ")

