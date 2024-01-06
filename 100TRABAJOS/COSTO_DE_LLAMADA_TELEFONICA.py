llamada = int()
costo = float()
print("CANTIDAD DE MINUTOS : ", end="")
llamada = int(input())
# Proceso 
if (llamada<=5):
	costo = llamada*0.9
	print("EL COSTO ES : $/.",costo)
else:
	costo = (5*0.9)+(llamada-5)*1.1
	print("EL COSTO ES : $/.",costo)

