# Estructura REPETITIVA PARA  
# Muesta 10 numeros de la serie fibonacci 
# Declarar Variables
cont = int()
a = int()
b = int()
c = int()
# Inicializar Variables.
a = 0
b = 1
c = 0
# Proceso y Salida
for cont in range(1,11):
	print(c," ")
	a = b
	b = c
	c = a+b

