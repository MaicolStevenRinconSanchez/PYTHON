
from random import randint


	color = int()
	desct = float()
	compra = float()
	desct = 0
	compra = 0
	print("VALOR DE COMPRA : S/.", end="")
	compra = float(input())
	print("PULSE UNA TECLA ... ", end="")
	tecla = input()
	print("")
	color = randint(0,4)
	if color==1:
		print("COLOR : BLANCO")
		desct = 1
	elif color==2:
		print("COLOR : VERDE")
		desct = 0.5
	elif color==3:
		print("COLOE : NEGRO")
		desct = 0.4
	elif color==4:
		print("COLOR : CELESTE")
		desct = 0.05
	elif color==5:
		print("COLOR : ROJO")
		desct = 0
	print("DESCUENTO  : S/.",desct)
	print("IMPORTE DESCT : S/.",compra*desct)
	print("PAGO FINAL : S/.",compra-(compra*desct))

