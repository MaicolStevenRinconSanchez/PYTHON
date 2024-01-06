# Declaracion de variables
h = int()
m = int()
s = int()
costo = float()
# ENTRADA
print("HORAS     : ", end="")
h = int(input())
print("MINUTOS   : ", end="")
m = int(input())
print("SEGUNDOS  : ", end="")
s = int(input())
# PROCESO.
costo = ((h*3600)+(m*60)+s)*0.25
# SALIDA
print("")
print("COSTO TOTAL : ",costo)

