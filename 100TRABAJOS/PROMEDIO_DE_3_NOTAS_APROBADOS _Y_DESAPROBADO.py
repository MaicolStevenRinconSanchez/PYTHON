n1 = int()
n2 = int()
n3 = int()
prom = float()
print("INGRESE NOTA 01 : ", end="")
n1 = int(input())
print("INGRESE NOTA 02 : ", end="")
n2 = int(input())
print("INGRESE NOTA 03 : ", end="")
n3 = int(input())
prom = (n1+n2+n3)/3
if (prom>10.5):
	print("APROBADO CON ",prom)
else:
	print("DESAPROBADO CON ",prom)

