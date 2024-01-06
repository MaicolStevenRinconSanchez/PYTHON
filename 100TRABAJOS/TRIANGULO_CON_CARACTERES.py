alt = int()
i = int()
j = int()
caract = str()
print("Altura del Triangulo", end="")
alt = int(input())
print("Ingrese un caracter", end="")
caract = input()
for i in range(1,alt+1):
	for j in range(1,i-alt+1):
		print(" ", end="")
	print("  ", end="")
	for j in range(1,((i*2)-1)+1):
		print(caract, end="")
	print(" ")

