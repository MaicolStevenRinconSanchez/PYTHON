# Declaracion de variables
hor = int()
min = int()
seg = int()
xseg = int()
# ENTRADA
print("CANTIDAD DE SEGUNDOS : ", end="")
xseg = int(input())
# PROCESO.
hor = int(xseg/3600)
min = int((xseg-(hor*3600))/60)
seg = int(xseg-((hor*3600)+(min*60)))
# SALIDA
print("HORAS    : ",hor)
print("MINUTOS  : ",min)
print("SEGUNDOS : ",seg)

