clave = int()
minutos = int()
print("CLAVES DE DESTINO")
print("(1) ESTADOS UNIDOS - $0.13")
print("(2) CANADA - $0.11")
print("(5) AMERICA DEL SUR - $0.52")
print("(6) AMERICA CENTRAL - $0.99")
print("(8) MEXICO - $0.17")
print("(9) EUROPA - $0.17")
print("(10) ASIA - $0.20")
print("(15) AFRICA - $0.59")
print("(20) OCEANIA - $0.28")
print("INGRESE CLAVE DESTINO : ", end="")
clave = int(input())
print("DURACION DE LA LLAMADA : ", end="")
minutos = int(input())
if (clave)==1:
	print("COSTO $.",minutos*0.13)
elif (clave)==2:
	print("COSTO $.",minutos*0.11)
elif (clave)==5:
	print("COSTO $.",minutos*0.52)
elif (clave)==6:
	print("COSTO $.",minutos*0.99)
elif (clave)==8:
	print("COSTO $.",minutos*0.17)
elif (clave)==9:
	print("COSTO $.",minutos*0.17)
elif (clave)==10:
	print("COSTO $.",minutos*0.20)
elif (clave)==15:
	print("COSTO $.",minutos*0.59)
elif (clave)==20:
	print("COSTO $.",minutos*0.28)
else:
	print("!!EROR EN CLAVE !!")

