# Calcular el producto de N numeros
n = int()
pro = int()
f = int()
pro = 1
print("VALOR DE N : ", end="")
n = int(input())
for f in range(1,n+1):
	print(f," ", end="")
	pro = pro*f
print(" ")
print("PRODUCTO DE ",n," ES : ",pro)

