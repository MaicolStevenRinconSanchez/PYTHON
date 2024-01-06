# Declaracion de variables
r = float()
h = float()
a = float()
v = float()
print("RADIO  : ", end="")
r = float(input())
print("ALTURA : ", end="")
h = float(input())
a = 2*pi*r*(h+r)
v = pi*(r*r)*h
print("AREA TOTAL DEL CILINDRO :",a,"cm2")
print("VOLUMEN DEL CILINDRO    :",v,"cm2")

