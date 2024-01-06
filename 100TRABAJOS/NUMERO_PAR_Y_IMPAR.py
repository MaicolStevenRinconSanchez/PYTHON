num = int()
c = int()
r = int()
re = int()
print "INGRESE NUMERO : ",
num = int(raw_input())
c = round(num/2)
r = c*2
re = num-r
if (re==0):
	print "NUMERO PAR"
else:
	print "NUMERO IMAPAR"

