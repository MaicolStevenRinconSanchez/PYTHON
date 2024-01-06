usuario = str()
clave = int()
# Entrada de Datos
print("INGRESE USUARIO", end="")
usuario = input()
print("ingrese clave:", end="")
clave = int(input())
# Proceso 
# Salida
if (usuario=="ADMIN" and clave==123456):
	print("ACCESO  PERMITIDO")
else:
	print("ACCESO DENEGADO")

