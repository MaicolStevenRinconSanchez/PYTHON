categoria = int()
sueldo = float()
bonificacion = float()
bonificacion = 0
print("Sueldo Base : S/.")
sueldo = float(input())
print("Categoria : 1.A - 2.B - 3.C - 4.D : ")
categoria = int(input())
if categoria==1:
	bonificacion = sueldo*0.1
elif categoria==2:
	bonificacion = sueldo*0.2
elif categoria==3:
	bonificacion = sueldo*0.3
elif categoria==4:
	bonificacion = sueldo*0.5
print("BONIFICACION : S/.",bonificacion)
print("SUELDO NETO  : S/.",sueldo+bonificacion)

