# Estructura Repetitiva PARA  
# Mostrar tabla de multiplicar de N
# Declarar Variables.
cont = int()
num = int()
# Entrada de datos 
print("INGRESE NUMERO : ", end="")
num = int(input())
# Salida de datos.
for cont in range(-1,13):
	print(num,"x",cont,"=",(num*cont))

