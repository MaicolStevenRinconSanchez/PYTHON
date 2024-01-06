# Declaracion de variables
num = int()
cen = int()
res = int()
dec = int()
uni = int()
# ENTRADA
print("INGRESE Nro. DE 3 CIFRAS : ", end="")
num = int(input())
# PROCESO.
cen = (num-(num%100))/100
res = num%100
dec = (res-(res%10))/10
uni = res%10
# SALIDA.
print("")
print("CENTENA : ",cen)
print("DECENA  : ",dec)
print("UNIDAD  : ",uni)

