import categorias as categoria

Incorrect = True

def verificarEdad() -> int:
    global Incorrect
    Incorrect = True
    while Incorrect:
        try:
            edad = int(input(f"Ingrese la edad del jugador : "))
        except ValueError:
            print(f"Ingrese un dato válido")
        else:
            Incorrect = False
    return edad

def buscarId(codigoJugador : str, jugadores : dict) -> str:
    data = jugadores.get(codigoJugador, -1)
    if (type(data) == dict):
        codigo = data.get("Id")
        return codigo

def regJugador(catJugador : int, edad_Jugador : int, jugadores : dict) -> dict:
    id = ""
    nombre = ""
    while (id == ""):
        id = input(f"Ingrese el código del jugador : ")
        idEncontrado = buscarId(id, jugadores)
        if (type(idEncontrado) == str):
            print(f"Ya existe un jugador con ese código")
            id = ""
    while (nombre == ""):
        nombre = input(f"Ingrese el nombre del jugador : ")
    categoriaJ = categoria.defCategoria(catJugador)
    jugador = {
        "Id" : id,
        "Nombre" : nombre,
        "Edad" : edad_Jugador,
        "Categoria" : categoriaJ,
        "PJ" : 0,
        "PG" : 0,
        "PP" : 0,
        "PA" : 0,
        "TP" : 0
    }
    return {id : jugador}

def buscarJugador(codJugador : str, jugadores : dict) -> str:
    data = jugadores.get(codJugador, -1)
    if (type(data) == dict):
        codigo = data.get("Id")
        return codigo
    else:
        print(f"No se encontró el jugador con el código {codJugador}")

def actualizarJugador(codJugador: str, jugadores : dict, puntosA : int, partidosG : int, partidosP : int, totalP : int):
    data = jugadores.get(codJugador, -1)
    PJ = data.get("PJ") + 1
    PG = data.get("PG") + partidosG
    PP = data.get("PP") + partidosP
    PA = data.get("PA") + puntosA
    TP = data.get("TP") + totalP
    data.update({"PJ" : PJ})
    data.update({"PG" : PG})
    data.update({"PP" : PP})
    data.update({"PA" : PA})
    data.update({"TP" : TP})

def mostrarTabla(jugadores : dict):
    print(f"")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("ID", "JUGADOR", "PJ", "PG", "PP", "PA", "TP"))
    print(f"-----------------------------------------------------------------------")
    for item in jugadores:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(jugadores[item]["Id"], jugadores[item]["Nombre"], jugadores[item]["PJ"], jugadores[item]["PG"], jugadores[item]["PP"], jugadores[item]["PA"], jugadores[item]["TP"]))
    print(f"")

def mostrarGanador(jugadores : dict):
    maxNombre = ""
    maxTPr = 0
    maxPA = 0
    for item in jugadores:
        if (jugadores[item]["TP"] > maxTPr):
            maxNombre = jugadores[item]["Nombre"]
            maxTPr = jugadores[item]["TP"]
            maxPA = jugadores[item]["PA"]
        elif (jugadores[item]["TP"] == maxTPr):
            if (jugadores[item]["PA"] > maxPA):
                maxNombre = jugadores[item]["Nombre"]
                maxTPr = jugadores[item]["TP"]
                maxPA = jugadores[item]["PA"]
    print(f"")
    print(f"EL/LA GANADOR/A ES : {maxNombre}")