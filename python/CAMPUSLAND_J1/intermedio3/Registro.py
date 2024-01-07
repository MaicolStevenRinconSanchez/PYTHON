
productos = []

def registrar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
    stock_maximo = int(input("Ingrese el stock máximo permitido: "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "valor_compra": valor_compra,
        "valor_venta": valor_venta,
        "stock_minimo": stock_minimo,
        "stock_maximo": stock_maximo,
        "proveedor": proveedor,
        "stock_actual": 0
    }
    productos.append(nuevo_producto)
    print(f"Producto {nombre} registrado exitosamente.\n")

def visualizar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Lista de productos registrados:")
        for producto in productos:
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Valor de compra: {producto['valor_compra']}")
            print(f"Valor de venta: {producto['valor_venta']}")
            print(f"Stock mínimo: {producto['stock_minimo']}")
            print(f"Stock máximo: {producto['stock_maximo']}")
            print(f"Proveedor: {producto['proveedor']}")
            print(f"Stock actual: {producto['stock_actual']}")
            print("--------------------------")

def actualizar_stock():
    codigo_producto = input("Ingrese el código del producto: ")
    
    # Presentar opciones de agregar o restar
    operacion = input("Seleccione la operación (A para agregar, R para restar): ").upper()

    try:
        cantidad = int(input("Ingrese la cantidad a agregar o restar al stock: "))
    except ValueError:
        print("Entrada inválida. La cantidad debe ser un número entero.")
        return

    for producto in productos:
        if producto["codigo"] == codigo_producto:
            if operacion == "A":
                producto["stock_actual"] += cantidad
            elif operacion == "R":
                producto["stock_actual"] -= cantidad
            else:
                print("Operación no válida. Use A para agregar o R para restar.")
                return

            print(f"Stock actualizado para el producto {codigo_producto}: {producto['stock_actual']}")
            break
    else:
        print(f"No se encontró el producto con código {codigo_producto}.")

def informe_productos_criticos():
        print("Informe de Productos Críticos:")
        productos_criticos = [producto for producto in productos if producto["stock_actual"] < producto["stock_minimo"]]

        if not productos_criticos:
            print("No hay productos críticos en este momento.")
            return

        for producto in productos_criticos:
            print(f"Producto: {producto['nombre']}, Stock Actual: {producto['stock_actual']}, Stock Mínimo: {producto['stock_minimo']}")

def calcular_ganancia_potencial():
    ganancia_total = 0
    for producto in productos:
        ganancia_total += (producto["valor_venta"] - producto["valor_compra"]) * producto["stock_actual"]

    print(f"Ganancia potencial total: {ganancia_total}")