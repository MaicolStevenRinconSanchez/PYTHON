e = 0
arreglo = []
total = 0
cont_pares = 0
arreglo_pares = []
impares = 0
arreglo_impares = []
cont_i = 0
cont_r = 0
cont_f = 0

print("Bienvenido, por favor escriba numeros enteros positivos,")
print("para totalizar escriba un numero entero negativo")
n = int(input("Escriba la cantidad de numeros que desea ingresar:  "))
arreglo = [1]*n

for e in range(len(arreglo)):
  while True:
    try:
      arreglo[e] = int(input("Ingrese un numero entero positivo o negativo:  "))
      break
    except ValueError:
      print("No es un numero entero. Intente de nuevo.")
   
  auxiliar = int(arreglo[e])
  if (auxiliar>0):
    total = total + 1
    if auxiliar % 2 == 0: 
      cont_pares = cont_pares + 1
      arreglo_pares.append(auxiliar)
    else:
      impares = impares + 1
      arreglo_impares.append(auxiliar)
    if (auxiliar<20):
      cont_i = cont_i + 1
    elif (auxiliar>= 20 and auxiliar<=50):
      cont_r = cont_r + 1
    elif (auxiliar>100):
      cont_f = cont_f + 1
  elif (auxiliar < 0):
    break
    
  arreglo.append(auxiliar)

suma_prom_pares = sum(arreglo_pares)
prom_pares = (suma_prom_pares/cont_pares)
suma_prom_impares = sum(arreglo_impares)
prom_impares = (suma_prom_impares/impares)
print(f"Total numeros ingresados: {total}")
print(f"Total numeros pares ingresados: {cont_pares}")
print(f"Promedio numeros pares ingresados: {prom_pares}")
print(f"Promedio numeros impares ingresados: {prom_impares}")
print(f"Total numeros menores a 20: {cont_i}")
print(f"Total numeros en 20 y 50: {cont_r}")
print(f"Total numeros mayores a 100: {cont_f}")