calcular_consumo_mensual =[]
arreglo_global = []
consumos_transportes = []
consumos_electricidad = []
factor_emision_electricidad = 0.5  # Este valor es un ejemplo, ajusta según tus necesidades

def ingreso_consumo(numero_electro):
    consumo = []
    for i in range(numero_electro):
        electrodomestico = input(f"Ingrese el nombre del electrodoméstico {i + 1}: ")
        consumo_electro = float(input(f"Ingrese el consumo mensual en kilovatios-hora (kWh) del electrodoméstico {i + 1}: "))
        consumo.append((electrodomestico, consumo_electro))
    return consumo

def calcular_emisiones_co2(consumo_electro):
    factor_emision = 0.5  # Este valor debe ajustarse según la fuente de generación de electricidad
    emisiones_co2 = sum(consumo[1] * factor_emision for consumo in consumo_electro)
    return emisiones_co2