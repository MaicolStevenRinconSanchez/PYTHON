# Mostrar si es numeros primos.
num = int()
divisi = int()
divi = int()
divisi = 0
print("INGRESE UN NUMERO : ", end="")
num = int(input())
for divi in range(1,num+1):
	if (num%divi)==0:
		divisi = divisi+1
if (divisi==2):
	print("NUMERO PRIMO ")
else:
	print("NO ES PRIMO ")

