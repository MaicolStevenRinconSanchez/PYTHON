# Muestra la siguiente grafica:
# 123456789
# 12345678
# 1234567
# 123456
# 12345
# 1234
# 123
# 12
# 1
f = float()
c = float()
serie = float()
for f in range(1,10):
	serie = 0
	for c in range(1,11-f):
		serie = (serie*10)+c
	print(serie)

