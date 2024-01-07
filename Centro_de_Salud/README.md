#hola
Este es un programa simple en Python diseñado para registrar información personal de estudiantes, calcular su Índice de Masa Corporal (IMC) y proporcionar un análisis de la salud de la comunidad estudiantil.

1.Registro de Estudiantes:

El programa solicita información personal de cada estudiante, incluyendo código, nombre, edad, altura y peso.
Se pueden registrar hasta 20 estudiantes. Después de cada registro, la pantalla se limpia para una mejor experiencia visual.
import IMC
import os
===========================================================  
ǁ  registro_estudiantil = []                              ǁ
ǁ  for i in range(20):                                    ǁ
ǁ      print(f"Datos del estudiante {i + 1}:")            ǁ
ǁ      estudiante = IMC.salud()                           ǁ
ǁ      registro_estudiantil.append(estudiante.copy())     ǁ
ǁ      os.system('cls')                                   ǁ
ǁ                                                         ǁ
===========================================================

2.Cálculo del IMC y Análisis de Salud:
El programa calcula el IMC para cada estudiante y muestra un mensaje que indica el estado de salud de cada uno.

for estudiante in registro_estudiantil:
    resultado_imc = IMC.imc(estudiante['codigo'], estudiante['nombre'], estudiante['edad'], estudiante['altura'], estudiante['peso'])
    print(f"Estudiante {estudiante['nombre']}  {resultado_imc}")
