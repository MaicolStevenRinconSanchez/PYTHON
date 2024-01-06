# Declaracion de variables
i = float()
n = float()
sumatoria = float()
v = float()
v1 = float()
v2 = float()
x = float()
x1 = float()
x2 = float()
ope = str()
sumatoria = 0
v = 4
v1 = 5
v2 = 1
x = 2
x1 = 0.5
ope = "-"
print("35. MUESTRA SERIE DE NÚMEROS.")
print("")
print("VALOR DE N : ", end="")
n = float(input())
# Proceso : Imprime la serie.
for i in range(1, int(n)+1):
  if (i!=n):
    print(v,"/",x," ",ope," ", end="")
  else:
    print(v,"/",x," ",ope," ...", end="")
  if ((i%2)==1):
    ope = "+"
    sumatoria = sumatoria+(v/x)
  else:
    ope = "-"
    sumatoria = sumatoria-(v/x)
  v = v+v1
  v1 = v1+v2
  v2 = v2+1
  x = x*x1
  x1 = (x1+x1)
# Salida de Datos
print("")
print("SUMATORIA : ",sumatoria)

