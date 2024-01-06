# Declaracion de variables
cont = int()
ventas = int()
empleados = int()
tv_h = int()
tv_m = int()
muj = int()
nom = str()
genero = str()
# Inicializar Variables
tv_h = 0
tv_m = 0
muj = 0
# ingreso de datos;
print("CANTIDAD DE EMPLEADOS : ", end="")
empleados = int(input())
print("")
# Proceso : Leer  los datos de N empleados
for cont in range(1,empleados+1):
	# Proceso : Solicita el ingreso de los datos de cada empleado
	print("EMPLEADO Nro ",cont,"/",empleados)
	print("NOMBRE : ", end="")
	nom = input()
	print("GÉNERO (H/M) : ", end="")
	genero = input()
	print("VENTAS : ", end="")
	ventas = int(input())
	print("")
	# Proceso : Obtener las ventas de hombre y mujeres
	if (genero=="H"):
		tv_h = tv_h+ventas
	else:
		tv_m = tv_m+ventas
		muj = muj+1
# Salida de datos
print("TOTAL DE VENTAS HOMBRES : ",tv_h)
print("TOTAL DE VENTAS MUJERES : ",tv_m)
print("")
print("PORCENTAJE DE MUJERES   : ",(muj*100)/empleados," %")

