num_hijos = int()
dias_no_laborales = int()
sueldobase = float()
sueldo_final = float()
sueldobase = 0
num_hijos = 0
dias_no_laborales = 0
sueldo_final = 0
# ingreso de datos
print("CALCULAR EL SUELDO FINAL DE UN EMPLEADO")
print("")
print("Ingres sueldo Base : $", end="")
sueldobase = float(input())
print("Ingrese Numero de Hijos ; ", end="")
num_hijos = int(input())
print("Ingrese Dias no Laborales Trabajados : ", end="")
dias_no_laborales = int(input())
sueldo_final = sueldobase+(num_hijos*100)+(dias_no_laborales*25)
# salida
print("")
print("SUELDO FINAL : $",sueldo_final)

