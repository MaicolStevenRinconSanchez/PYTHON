apro = float()
desa = float()
pora = float()
pord = float()
# Ingrese de Datos
print("MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS")
print("")
print("INGRESE CANTIDAD DE ALUMNOS APROBADOS : ", end="")
apro = float(input())
print("INGRESE CANTIDAD DE ALUMNOS DESAPROBADOS : ", end="")
desa = float(input())
print("")
# Proceso 
pora = (apro*100)/(apro+desa)
pord = (desa*100)/(apro+desa)
# Salida
print("APROBADOS : ",(round(pora*100)/100),"%")
print("DESAPROBADOS : ",(round(pord*100)/100),"%")
  
