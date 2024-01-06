nom = str()
sueldob = float()
boni = float()
sueldof = float()
hijos = int()
boni = 0
sueldof = 0
print("09. CALCULAR EL SUELDO FINAL ")
print("Ingrese Nombre : ", end="")
nom = input()
print("Sueldo Basico  : $/.", end="")
sueldob = float(input())
print("Nrio. de hijos : ", end="")
hijos = int(input())
if (hijos>0):
	boni = sueldob*0.7
sueldof = sueldob+boni
print("")
print("BONIFICACION : $/.",boni)
print("SUELDO FINAL : $/.",sueldof)

