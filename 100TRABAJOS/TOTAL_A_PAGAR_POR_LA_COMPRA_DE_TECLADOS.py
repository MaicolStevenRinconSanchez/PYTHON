cantidad = int()
costo = int()
print("Cantidad a comprar : ", end="")
cantidad = int(input())
if cantidad==1 or cantidad==2 or cantidad==3:
	costo = 15
elif cantidad==4 or cantidad==5 or cantidad==6 or cantidad==7 or cantidad==8:
	costo = 11
else:
	costo = 10
print("Costo por teclado : S/.",costo)
print("Total a Pagar : S/.",costo*cantidad)

