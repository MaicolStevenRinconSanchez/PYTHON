# Declaracion de variables
x = int()
edad = int()
dia = int()
mes = int()
anio = int()
diax = int()
mesx = int()
aniox = int()
dni = str()
genero = str()
# Actualiza los datos de  la fecha Actual
diax = 21
mesx = 10
aniox = 2022
edad = 0
 
for x in range(1,11):
	print("DNI : ", end="")
	dni = input()
	print("DiA DE NACIMIENTO: ", end="")
	dia = int(input())
	print("MES DE NACIMIENTO: ", end="")
	mes = int(input())
	print("AñO DE NACIMIENTO: ", end="")
	anio = int(input())
	print("GeNERO (H/M): ", end="")
	genero = input()
	print("FECHA ACTUAL : ",diax,"/",mesx,"/",aniox)
	edad = aniox-anio
	if (mes>mesx):
		edad = edad-1
	else:
		if (mes==mesx and dia>diax):
			edad = edad-1
	print("EDAD : ",edad," años", end="")
	print(" ")
	if (edad>=8):
		print("RECIBE TABLET")
	else:
		if (edad==6):
			if (genero=="H"):
				print("RECIBE CARRITO")
			else:
				print("RECIBE MU�ECA")
	print(" ")

