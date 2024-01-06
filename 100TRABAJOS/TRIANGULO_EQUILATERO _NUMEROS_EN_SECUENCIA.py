# Declaracion de variables
x = int()
z = int()
num = int()
val = int()
f = int()
contador = int()
espa = str()
num = 0
val = 1
contador = 1
# Solicitar un numero mientras el numero sea menor a 3
print("MUESTRA GRAFICA DE NOMEROS COMO TRIANGULO.")
while (num<3):
	print("INGRESE NUMERO : ", end="")
	num = int(input())
print("")
# Proces : Muestra un triangulo de numero.
for x in range(1,num+1):
	espa = ""
	for z in range(1,(num-x)+1):
		espa = espa+" "
	print(espa, end="")
	# Muestra espacios vacios
	contador = 1
	for f in range(1,val+1):
		print(contador, end="")
		if (contador==9):
			contador = 0
		else:
			contador = contador+1
	val = val+2
	print("")

