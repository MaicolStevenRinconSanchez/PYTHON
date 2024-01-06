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
# Inicializando variabl
c = 0
s = 0
d = 0
l = 0
r = 0
m = 0
consonante = 0
refran = ""
# ingreso de Datos
print("Ingrese Refran : ")
ref = input()
# Proceso : Eliminar los espacios en blanco del refran ingresado
for f in range(len(ref)+1):
	if (ref[f-1:f]!=" "):
		refran = refran+ref[f-1:f]
# Proceso  : Contar cuantas letras C,S,D,L,R Y MHAY
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
# Salida de Datos
print("CANTIDA DE C : ",c)
print("CANTIDA DE S : ",s)
print("CANTIDA DE D : ",d)
print("CANTIDA DE L : ",l)
print("CANTIDA DE R : ",r)
print("CANTIDA DE M : ",m)
print("CANTIDA DE CONSONANTES : ",consonante)

