	# Declaracion de variables
	man = int()
	noc = int()
	cont = int()
	tipo = int()
	cantidad = int()
	bus = int()
	van = int()
	micro = int()
	tarifa = float()
	turno = str()
	tarifa = 0
	bus = 0
	van = 0
	micro = 0
	man = 0
	noc = 0
	# Ingreso de Datos
	print(" GANANCIAS DE UNA GARITA DE CONTROL.")
	print("CANTIDAD DE VEHICULOS ", end="")
	cantidad = int(input())
	print(" ")
	# Proceso  : Calcula la tarifa Segun  el vehiculo
	for cont in range(1,cantidad+1):
		print(">> TIPO DE VEHÍCULO Nro ",cont,"/",cantidad," : ")
		print("1. Ómnibus")
		print("2. Minivan")
		print("3. Micro")
		print("OPC : ", end="")
		tipo = int(input())
		if (tipo)==1:
			tarifa = 13
			bus = bus+tarifa
		elif (tipo)==2:
			tarifa = 10
			van = van+tarifa
		elif (tipo)==3:
			tarifa = 8
			micro = micro+tarifa
		print("TURNO (M/N): ", end="")
		turno = input()
		if (turno=="M"):
			man = man+tarifa
		else:
			noc = noc+tarifa
		print(" ")
	# Salida de Datos
	print(" ")
	print("IMPORTE DE TURNO MAÑANA :",man)
	print("IMPORTE DE TURNO NOCHE :",noc)
	print(" ")
	print("IMPORTE DE ÓMNIBUS :",bus)
	print("IMPORTE DE MINIVAN :",van)
	print("IMPORTE DE MICRO :",micro)

