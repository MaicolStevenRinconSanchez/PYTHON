
Sistema de Monitoreo Sísmico y Riesgo
Este programa en Python permite registrar la actividad sísmica de ciudades, calcular promedios y proporcionar un informe de riesgo.
A continuación, se presenta una descripción del código y su uso.

1.Registro de Ciudades:

El programa permite al usuario registrar ciudades y sus respectivos sismos.
Se puede registrar un máximo de 5 ciudades, y para cada ciudad, ingresar la magnitud de sismos.

import os
import registro_ciudad as rc

arreglo_ciudades = []
ya_ingresados = []

print("Bienvenidos al sistema de monitoreo sísmico")
print("A continuación aparecerá un menú para registrar la actividad sísmica de algunas ciudades")

n = int(input("Ingrese el número de sismos que va a agregar en las ciudades:  "))

while True:
    # ... (resto del código)

2.Registro de Sismos:

Se puede registrar la magnitud de sismos para cada ciudad.
El programa valida si la ciudad ya ha registrado sismos previamente.

elif opMenu == 2:
  (código para el registro de sismos)

3.Buscar Sismos por Ciudad:

Permite al usuario buscar y visualizar los sismos registrados para una ciudad específica.

elif opMenu == 3:
  (código para buscar sismos por ciudad)

4.Informe de Riesgo:

Proporciona un informe de riesgo clasificando las ciudades según el promedio de magnitudes de sismos.

elif opMenu == 4:
  (código para generar el informe de riesgo)

5.Salir del Programa:
Finaliza la ejecución del programa.
elif opMenu == 5:
    isActive = False



