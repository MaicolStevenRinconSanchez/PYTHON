# Numeros del rango de menor a mayor
a = int()
b = int()
n = int()
print("NUMERO A : ", end="")
a = int(input())
print("NUMERO B : ", end="")
b = int(input())
if (a<b):
		for n in range(a+1,b):
			print(n)
else:
		for n in range(b+1,a):
			print(n)

