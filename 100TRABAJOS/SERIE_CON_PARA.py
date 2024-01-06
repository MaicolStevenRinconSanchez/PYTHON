# Mostrar la serie: 1+ 2/3 + 3/5 + 4/7...
suma = float()
n = int()
i = int()
d = int()
print("VALOR DE N : ", end="")
n = int(input())
suma = 1
d = 3
if (n>1):
	print(suma," + ", end="")
	for i in range(2,n+1):
		if (i==n):
			print(i,"/",d, end="")
		else:
			print(i,"/",d," + ", end="")
		suma = suma+(i/d)
		d = d+2
print("")
print("La suma es : ",suma)

