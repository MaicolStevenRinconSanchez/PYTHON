altura = int()
n = int()
j = int()
while True:
	print("Altura del rombo : ", end="")
	altura = int(input())
	if (altura%2)==1: break
for n in range(1,altura+1,2):
	for j in range(altura-n):
		print  ("",end=" ")
	for j in range(1,n+1):
		print("*", end=" ")
	print (" ")
 
for n in range((altura-2),0,-2):
	for j in range(altura-n):
		print("", end=" ")
	for j in range(1,n+1):
			
		print("*", end=" ")
	print(" ")

