precio = float()
igv = float()
monto = float()
cant = int()
igv = 0
monto = 0
print("05.CALCULAR IGV SEGUN EL MONTO DE COMPRA")
print("INGRESE PRECIO : $/.", end="")
precio = float(input())
print("INGRESE CANTIDAD : ", end="")
cant = int(input())
monto = (precio*cant)
if (monto>100):
	# 18%
	igv = monto*0.18
print("")
print("TOTAL         : $/.",monto)
print("IGV 18%       :$/.",igv)
print("TOTAL A PAGAR :$/.",(monto+igv))

