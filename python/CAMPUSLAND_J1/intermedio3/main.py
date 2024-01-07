import os
from Registro import (
    registrar_producto,
    visualizar_productos,
    actualizar_stock,
    informe_productos_criticos,
    calcular_ganancia_potencial
)

# Menú principal
while True:
    print("\n1. Registrar Producto")
    print("2. Visualizar Productos")
    print("3. Actualizar Stock")
    print("4. Informe de Productos Críticos")
    print("5. Calcular Ganancia Potencial")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        visualizar_productos()
    elif opcion == "3":
        actualizar_stock()
    elif opcion == "4":
        informe_productos_criticos()
    elif opcion == "5":
        calcular_ganancia_potencial()
        if opcion == "6":
          print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")