# Muestra la siguiente grafica:
# 999999999
# 88888888
# 7777777
# 666666
# 55555
# 4444
# 333
# 22
# 1
f = float()
c = float()
s = float()
serie = float()
for f in range(1,10):
	s = 0
	serie = 0
	for c in range(1,11-f):
		s = (10-f)
		serie = (serie*10)+s
	print(serie)

