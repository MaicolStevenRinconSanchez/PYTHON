import IMC
import os

registro_estudiantil = []

# Recopilar datos de estudiantes
for i in range(20):  # Asumiendo que queremos registrar 2 estudiantes
    print(f"Datos del estudiante {i + 1}:")
    estudiante = IMC.salud()
    registro_estudiantil.append(estudiante.copy())
os.system('cls')
# Calcular el IMC para cada estudiante
for estudiante in registro_estudiantil:
    resultado_imc = IMC.imc(estudiante ['codigo'],estudiante['nombre'], estudiante['edad'], estudiante['altura'], estudiante['peso'])
    print(f"Estudiante {estudiante['nombre']}  {resultado_imc}")
#3. Teniendo en cuenta el punto 2 se requiere tener el registro de 20 estudiantes y poder determinar
#el estado de salud de la comunidad estudiantil. El programa debe mostrar el siguiente reporte:}

# a. Cuantos estudiantes se encuentran en el peso ideal.
# b. Cuantos estudiantes se encuentran en obesidad grado I
# c. Cuantos estudiantes se encuentran en obesidad grado II
# d. Cuantos estudiantes se encuentran en obesidad grado III
# e. Cuantos estudiantes se encuentran en Sobrepeso 