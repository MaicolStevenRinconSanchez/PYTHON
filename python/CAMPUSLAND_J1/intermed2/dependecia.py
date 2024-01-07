# dependencia.py

arreglo_dependencia = []

def ingreso_dependencia():
    rta = "S"
    while rta in ["S", "s"]:
        arreglo_dependencia.append(input("Escriba el nombre de la dependencia: "))
        rta = input("Desea registrar otra dependencia? S(si) o N(no u otra letra): ").upper()
        if rta == "N":
            break

    return arreglo_dependencia
