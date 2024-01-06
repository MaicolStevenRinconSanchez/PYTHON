# Declaracion de variables
refran = str()
ref = str()
letra = str()
f = int()
c = int()
s = int()
d = int()
l = int()
r = int()
m = int()
consonante = int()
c = 0
s = 0
d = 0
l = 0
r = 0
m = 0
consonante = 0
refran = ""
#Proceso: Contar la cantidad de vocales.
print(" MUESTRA LAS LETRAS F, C, S, D, L, R, M.")
#Obtine una letra de la frase
print("Ingrese Refran : ")
ref = input()
for f in range(len(ref)+1):
	if (ref[f-1:f]!=" "):
		refran = refran+ref[f-1:f]
for f in range(1,len(refran)+1):
	letra = str.upper(refran[f-1:f])
	if (letra=="C"):
		c = c+1
	if (letra=="S"):
		s = s+1
	if (letra=="D"):
		d = d+1
	if (letra=="L"):
		l = l+1
	if (letra=="R"):
		r = r+1
	if (letra=="M"):
		m = m+1
	if (letra!="A" and letra!="E" and letra!="I" and letra!="O" and letra!="U"):
		consonante = consonante+1
		#Salid de Datos
print("CANTIDA DE C : ",c)
print("CANTIDA DE S : ",s)
print("CANTIDA DE D : ",d)
print("CANTIDA DE L : ",l)
print("CANTIDA DE R : ",r)
print("CANTIDA DE M : ",m)
print("CANTIDA DE CONSONANTES : ",consonante)

