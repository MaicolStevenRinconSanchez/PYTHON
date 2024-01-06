opc = int()
area = float()
base = float()
altura = float()
print("MENU DE OPCIONES DE UN TRIANGULO")
print("__________________________________")
print("1.Area de un triangulo, dada la base y la altura")
print("2.Base de un triangulo, dada la altura y el area")
print("3.Altura de un triangulo. dada la base y el area")
print("Selecciona una opcion : ", end="")
opc = int(input())
print("")
if opc==1:
	print("BASE : ", end="")
	base = float(input())
	print("ALTURA : ", end="")
	altura = float(input())
	area = (base*altura)/2
	print("EL AREA ES : ",area)
elif opc==2:
	print("ALTURA : ", end="")
	altura = float(input())
	print("AREA   : ", end="")
	area = float(input())
	base = (area*2)/altura
	print("LA BASE ES : ",base)
elif opc==3:
	print(" BASE : ", end="")
	base = float(input())
	print(" AREA : ", end="")
	area = float(input())
	altura = (area*2)/base
	print("LA ALTURA ES : ",altura)
else:
	print("ERROR.. OPCION INCORRECTA")

