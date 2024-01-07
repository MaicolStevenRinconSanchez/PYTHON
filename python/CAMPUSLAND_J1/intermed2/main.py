# main.py
import os
import dependecia
import consumos

menu = "1. Registrar Dependencia\n2. Registrar consumo por dependencia\n3. Ver CO2 producido\n4. Dependecia que produce mayor CO2\n5. Salir\n:)"
isActive = True

registro = []

print("Bienvenidos a la calculadora de CO2")
print("A continuación aparecerá un menú de opciones con el que puede realizar los cálculos")

while isActive:
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if opMenu == 1:
            registro = dependecia.ingreso_dependencia()
            print(registro)
        elif opMenu == 2:
            if not registro:
                print("Primero debe registrar al menos una dependencia.")
                continue

            dependencia_enum = list(enumerate(registro))
            try:
                print("Elija el número de la dependencia a la que va a agregar los electrodomésticos:  ")
                for i in range(len(registro)):
                    print(dependencia_enum[i])
                num_depen = int(input(""))
            except ValueError:
                print("Lo escrito no es válido, digite de nuevo por favor")

            if any(dep[0] == registro[num_depen] for dep in consumos.arreglo_global):
                print("Ya ha registrado el consumo para esta dependencia")
            else:
                print("")
                numero_electro = int(input("Escriba el número de electrodomésticos que tiene la dependencia: "))
                arreglo_grande = consumos.ingreso_consumo(numero_electro)
                union_arreglos = [registro[num_depen], arreglo_grande]
                consumos.arreglo_global.append(union_arreglos)
                print(f"Dependencias con sus respectivos consumos: {consumos.arreglo_global}")

        elif opMenu == 3:
            if not registro:
                print("Primero debe registrar al menos una dependencia.")
                continue

            dependencia_enum = list(enumerate(registro))
            try:
                print("Elija el número de la dependencia para ver las emisiones de CO2:  ")
                for i in range(len(registro)):
                    print(dependencia_enum[i])
                num_depen = int(input(""))
            except ValueError:
                print("Lo escrito no es válido, digite de nuevo por favor")

            for dependencia_consumos in consumos.arreglo_global:
                if dependencia_consumos[0] == registro[num_depen]:
                    emisiones_co2 = consumos.calcular_emisiones_co2(dependencia_consumos[1])
                    print(f"CO2 producido por la dependencia: {emisiones_co2} tCO2eq")
        elif opMenu == 4:
            if not registro:
                print("Primero debe registrar al menos una dependencia.")
                continue

            mayor_emision_dependencia = consumos.arreglo_global[0][0]
            mayor_emision_valor = consumos.calcular_emisiones_co2(consumos.arreglo_global[0][1])

            for dependencia_consumos in consumos.arreglo_global[1:]:
                emisiones_co2 = consumos.calcular_emisiones_co2(dependencia_consumos[1])
                if emisiones_co2 > mayor_emision_valor:
                    mayor_emision_dependencia = dependencia_consumos[0]
                    mayor_emision_valor = emisiones_co2
                    print(f"\nLa dependencia que produce mayor CO2 es '{mayor_emision_dependencia}' con {mayor_emision_valor} tCO2eq")
        elif opMenu == 5:
                isActive = False

    print("Gracias por usar la calculadora de CO2. ¡Hasta luego!")