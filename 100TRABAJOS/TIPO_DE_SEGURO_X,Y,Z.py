seguro = int()
print("TIPOS DE SEGURO")
print("1. x")
print("2. Y")
print("3. Z")
print("OPCION : ", end="")
seguro = int(input())
if seguro==1:
	print("pago mensual : $45")
elif seguro==2:
	print("pago mensual : $30")
elif seguro==3:
	print("pago mensual : $15")
else:
	print("Error en el tipo de seguro ")

