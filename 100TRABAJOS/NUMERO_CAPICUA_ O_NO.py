num = int()
c1 = int()
r1 = int()
c2 = int()
r2 = int()
print("INGRESE  UN NUMERO DE 3 CIFRAS : ", end="")
num = int(input())
# Proceso 
c1 = (num-(num%100))/100
r1 = num%100
c2 = (r1-(r1%10))/10
r2 = r1%10
# Salida 
if (num==((r2*100)+(c2*10)+c1)):
	print("NUMERO CAPICUA")
else:
	print("NO ES UN NUMERO CAPICUA")

