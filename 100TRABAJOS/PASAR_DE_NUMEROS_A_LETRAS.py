num = int()
dec = int()
uni = int()
decena = str()
unidad = str()
print("PASAR DE NUMEROS A LETRAS")
print("INGRESE NUMERO DE HASTA 2 CIFRAS : ", end="")
num = int(input())
if (num>0 and num<100):
	if (num>10 and num<16):
		if num==11:
			print("ONCE")
		elif num==12:
			print("DOCE")
		elif num==13:
			print("TRECCE")
		elif num==14:
			print("CATORCE")
		elif num==15:
			print("QUINCE")
	else:
		dec = (num-(num%10))/10
		uni = (num%10)
		if dec==1:
			decena = "DIEZ"
		elif dec==2:
			decena = "VEINTE"
		elif dec==3:
			decena = "TREINTA"
		elif dec==4:
			decena = "CUARENTA"
		elif dec==5:
			decena = "CINCUENTA"
		elif dec==6:
			decena = "SESENTA"
		elif dec==7:
			decena = "SETENTA"
		elif dec==8:
			decena = "OCHENTA"
		elif dec==9:
			decena = "NOVENTA"
		if (uni!=0):
			if (uni)==1:
				unidad = "UNO"
			elif (uni)==2:
				unidad = "DOS"
			elif (uni)==3:
				unidad = "TRES"
			elif (uni)==4:
				unidad = "CUATRO"
			elif (uni)==5:
				unidad = "CINCO"
			elif (uni)==6:
				unidad = "SEIS"
			elif (uni)==7:
				unidad = "SIETE"
			elif (uni)==8:
				unidad = "OCHO"
			elif (uni)==9:
				unidad = "NUEVE"
			if (dec==1):
				decena = "DIECI"
			if (dec==2):
				decena = "VENTI"
			if (dec>2 and dec<10):
				print(decena," Y ",unidad)
			else:
				print(decena,"",unidad)
		else:
			print(decena)
else:
	print("NUMERO INCORRECTO. ... ")

