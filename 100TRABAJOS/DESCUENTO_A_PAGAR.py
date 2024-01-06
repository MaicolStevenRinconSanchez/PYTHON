monto = float()
desct = float()
print("MONTO DE COMPRA : $/.", end="")
monto = float(input())
# Salida
if (monto>=350):
	desct = monto*0.35
	print("DESCUENTO ES DE 35%: $/.",desct)
else:
	desct = monto*0.10
	print("DESCUENTO ES DE 10% : $/. ",desct)
print("MONTO A PAGAR ; $/.",(monto-desct))

