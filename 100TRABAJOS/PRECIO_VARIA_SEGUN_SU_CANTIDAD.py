cantidad = int()
costo = float()
print("INGRESE CANTIDAD A COMPRAR : ", end="")
cantidad = int(input())
if cantidad==1 or cantidad==2 or cantidad==3:
	costo = 15
elif cantidad==4 or cantidad==5 or cantidad==6 or cantidad==7 or cantidad==8:
	costo = 11
else:
	costo = 10
print("COSTO POR TECLADO : S/.",costo)
print("TOTAL A PAGAR     : S/.",costo*cantidad)

