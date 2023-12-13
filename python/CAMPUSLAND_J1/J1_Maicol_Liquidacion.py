#sirve para borra pantalla pero en visualcode
"""import os
os.system("cls")"""
if __name__ == '__main__':
	nombreempleado = str()
	rangoempleado = str()
	continuar = str()
	subtrasporte = float()
	bonorango = float()
	aportesocial = float()
	valordia = float()
	horastrabajadas = float()
	valorbono = float()
	valorbase = float()
	salario = float()
	diasincapacidad = float()
	diastra = float()
	llamadosatencion = int()
	salario = 0
	diastra = 30
	valorbase = 1300000
	valordia = valorbase/30
	subtransporte = valorbase*0.1
	aportesocial = valorbase*0.04
	salariobase=valorbase*0.1
	llamadosatencion = valorbase*0.9
	print("Ingresa el Nombre del Empleado")
	nombreempleado = input()
	print("Ingresa el Rango de Empleado")
	print("A. Mensajero")
	print("B. Administrativo")
	print("C. IT Soluciones")
	print("D. Seguridad")
	rangoempleado = input()
	if rangoempleado=="A":
		valorbono = subtransporte
	elif rangoempleado=="B":
		valorbono2 = salariobase
	elif rangoempleado=="C":
		valorbono3 = salariobase
	elif rangoempleado=="D":
		valorbono4 = 300000
	else:
		print("Error rango No Reconocido Intenta de Nuevo mas Tarde")
	print("El Empleado Cuenta con Llamados de Atencion (s/n)")
	continuar = input()
	if continuar=="s":
		salario = llamadosatencion
	else:
		salario = valorbase
	print("El Empleado Cuenta con Dias de Incapacidad s/n")
	continuar = input()
	if continuar=="s":
		print("Cuantos dias? 1,2,3")
		diasincapacidad = float(input())
		diastra = (30-diasincapacidad)
		valordia = (salario/diastra)
		salario = (diastra*valordia)
	print("El Empleado Cuenta con Horas Extras s/n")
	continuar = input()
	if continuar=="s":
		print("Cuantas Horas? 1,2,3")
		horastrabajadas = float(input())
		salario = salario+(horastrabajadas*20000)
	print("****************************")
	print (f"nombre :{nombreempleado} ")
	print("Salario Base: ",valorbase)
	print("Dias Trabajados: ",diastra)
	print("Valor Dia: ",valordia)
	# o salario / diasTra
	print("Valor Bono: ",valorbono)
	print("Valor Descuento por Penalizacion: ",llamadosatencion)
	print("Seguridad Social: ",aportesocial)
	print("Total a Pagar: ",salario+valorbono)

	# sirve para presionar continuar pero en visualcode


	"""os.sytem("pause")"""

