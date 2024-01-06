# Estructura REPETITIVA PARA  
# Muestra nombre y prromedio de alumno con mayor nota.
cont = int()
xpro = float()
pro = float()
xnom = str()
nom = str()
xpro = 0
for cont in range(1,6):
	print("NOMBRE : ", end="")
	nom = input()
	print("PROMEDIO : ", end="")
	pro = float(input())
	if (xpro<pro):
		xpro = pro
		xnom = nom
print("ALUMNO CON MAYOR NOTA : ",xnom)
print("PROMEDIO              : ",xpro)

