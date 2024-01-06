i = int()
n = int()
r = int()
v = int()
a = int()
c = str()
mcolor = str()
r = 0
v = 0
a = 0
print("CANTIDAD DE PERSONAS : ", end="")
n = int(input())
for i in range(1,n+1):
	print("PERSONA Nro.",i," ", end="")
	c = ""
	while (c!="ROJO" and c!="VERDE" and c!="AZUL"):
		print("[ROJO - VERDE - AZUL] :", end="")
		c = input()
		c = str.upper(c)
	if (c=="ROJO"):
		r = r+1
	else:
		if (c=="VERDE"):
			v = v+1
		else:
			a = a+1
print("")
if (r==v and v==a):
	mcolor = "TODOS LOS COLORES TIENEN LA MISMA CANTIDAD DE VOTOS"
else:
	if (r==v) and (r>a) and (v>a):
		mcolor = "ROJO Y VERDE SON  MAS ESCOGIDO"
	else:
		if (a==r) and (a>v) and (r>v):
			mcolor = "AZUL Y ROJO SON MAS ESCOGIDO"
		else:
			if (a==v) and (a>r) and (v>r):
				mcolor = "VERDE Y AZUL SON MAS ESCONGIDO"
			if (r>v and r>a):
				mcolor = "ROJO"
			else:
				if (v>r and v>a):
					mcolor = "VERDE"
					if (a>r and a>v):
						mcolor = "VERDE"
print("CANTIDAD DE COLOR ROJO   : ",r)
print("CANTIDAD DE COLOR VERDE  : ",v)
print("CANTIDAD DE COLOR AZUL   : ",a)
print("EL COLOR MAS ESCOGIDO ES : ",mcolor)

