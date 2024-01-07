
Este proyecto consiste en una aplicación simple para la gestión de inventario de productos. Permite registrar nuevos productos, visualizar la lista de productos, actualizar el stock, generar informes de productos críticos y calcular la ganancia potencial.

Estructura del Proyecto
main.py: Archivo principal que ejecuta la aplicación y gestiona el menú de opciones.
Registro.py: Contiene funciones relacionadas con el registro de productos, visualización, actualización de stock, informes y cálculos de ganancia.
Funcionalidades
Registrar Producto:

Ingresa información detallada sobre un nuevo producto, incluyendo código, nombre, valor de compra, valor de venta, stock mínimo, stock máximo y proveedor.
El stock actual se inicializa en cero y se actualiza posteriormente.
Visualizar Productos:

Muestra la lista de productos registrados, incluyendo detalles como código, nombre, valores, stock mínimo, stock máximo, proveedor y stock actual.
Actualizar Stock:

Permite agregar o restar unidades al stock de un producto específico.
Selecciona la operación (A para agregar, R para restar) y proporciona la cantidad.
Informe de Productos Críticos:

Genera un informe de productos que tienen un stock actual por debajo del stock mínimo permitido.
Muestra detalles como nombre del producto, stock actual y stock mínimo.
Calcular Ganancia Potencial:

Calcula la ganancia potencial total sumando las ganancias individuales de cada producto.
La ganancia de un producto se calcula como la diferencia entre el valor de venta y el valor de compra,
multiplicada por el stock actual.
