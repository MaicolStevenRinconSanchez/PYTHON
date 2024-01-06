n1 = int()
n2 = int()
n3 = int()
prom = int()
print("Ingrese Nota 1 : ", end="")
n1 = int(input())
print("Ingrese Nota 2 : ", end="")
n2 = int(input())
print("Ingrese Nota 3 : ", end="")
n3 = int(input())
prom = round((n1+n2+n3)/3)
if prom==0 or prom==1 or prom==2 or prom==3 or prom==4 or prom==5 or prom==6 or prom==7 or prom==8 or prom==9 or prom==10:
	print("NIVEL MALO")
elif prom==11 or prom==12 or prom==13:
	print("NIVEL REGULAR")
elif prom==14 or prom==15 or prom==16:
	print("NIVEL BUENO")
elif prom==17 or prom==18 or prom==19 or prom==20:
	print("NIVEL MUY BUENO")

