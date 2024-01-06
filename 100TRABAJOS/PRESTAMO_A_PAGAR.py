# Declaracion de variables
monto = float()
intereses = float()
totalp = float()
meses = int()
# Asugnacion de valor constante.
monto = 1000
# ENTRADA.
print("Nro de meses : ", end="")
meses = int(input())
# PROCESO.
intereses = (monto*(meses*0.02))
totalp = monto+intereses
# SALIDA
print("INTERESES      : ",intereses)
print("TOTAL A PAGAR  : ",totalp)

