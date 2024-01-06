# Declaracion de variables
costo = float()
iva = float()
totpagar = float()
print("")
print("Costo de la Casa : $/ ", end="")
costo = float(input())
print("Valor de IVA     : % ", end="")
iva = float(input())
print("")
totpagar = costo+(costo*(iva/100))
print("IVA DE ",iva,"% :$/.",(costo*(iva/100)))
print("TOTAL A PAGAR   :$/.",totpagar)

