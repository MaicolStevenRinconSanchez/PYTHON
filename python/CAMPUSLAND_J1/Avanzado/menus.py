import os
import jugadores as jugador
import partidos as partido

jugadoresNova = {}
jugadoresInterme = {}
jugadoresAvanza = {}
menuP = "1. Registrar Jugador\n2. Registrar Partido\n3. Tabla de puntajes\n4. Ganador de cada categoría\n5. Salir"
menuRegJ = "1. Novato (15-16 años)\n2. Intermedio (17-20 años)\n3. Avanzado (Mayor de 20 años)\n4. Volver"
headerP = """
***********************************************
BIENVENIDO AL TORNEO DE TENIS DE MESA DE CAMPUS
***********************************************
"""
headerRJ = """
***********************************************
REGISTRO DE JUGADORES
***********************************************
"""
headerRP = """
***********************************************
REGISTRO DE PARTIDOS
***********************************************
"""
headerTablas = """
***********************************************
TABLA DE PUNTAJES
***********************************************
"""
headerGanadores = """
***********************************************
GANADORES POR CATEGORÍA
***********************************************
"""
hasError = True

def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(headerP)
    print(menuP)
    while (hasError):
        try:
            print(f"")
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Ingrese un dato válido")
            hasError = True

def menuRegistroJ():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerRJ)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                if (len(partido.partidosNovatos) > 0):
                    print(f"El torneo ya comenzó, no se pueden registrar más participantes")
                else:
                    edad = jugador.verificarEdad()
                    if (edad >= 15 and edad <= 16):
                        jugadoresNova.update(jugador.regJugador(opMenu, edad, jugadoresNova))
                    else:
                        print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 2):
                if (len(partido.partidosIntermedios) > 0):
                    print(f"El torneo ya comenzó, no se pueden registrar más participantes")
                else:
                    edad = jugador.verificarEdad()
                    if (edad >= 17 and edad <= 20):
                        jugadoresInterme.update(jugador.regJugador(opMenu, edad, jugadoresInterme))
                    else:
                        print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 3):
                if (len(partido.partidosAvanzados) > 0):
                    print(f"El torneo ya comenzó, no se pueden registrar más participantes")
                else:
                    edad = jugador.verificarEdad()
                    if (edad > 20):
                        jugadoresAvanza.update(jugador.regJugador(opMenu, edad, jugadoresAvanza))
                    else:
                        print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")
            
def menuRegistroP():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerRP)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                if (len(jugadoresNova) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partidoF = partido.regPartidos(opMenu)
                    if (type(partidoF) != dict):
                        print(f"No se puede registrar un mismo partido 2 veces")
                    else:
                        partido.partidosNovatos.update(partidoF)
            elif (opMenu == 2):
                if (len(jugadoresInterme) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partidoF = partido.regPartidos(opMenu)
                    if (type(partidoF) != dict):
                        print(f"No se puede registrar un mismo partido 2 veces")
                    else:
                        partido.partidosIntermedios.update(partidoF)
            elif (opMenu == 3):
                if (len(jugadoresAvanza) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partidoF = partido.regPartidos(opMenu)
                    if (type(partidoF) != dict):
                        print(f"No se puede registrar un mismo partido 2 veces")
                    else:
                        partido.partidosAvanzados.update(partidoF)
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")

def menuTablas():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerTablas)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                jugador.mostrarTabla(jugadoresNova)
            elif (opMenu == 2):
                jugador.mostrarTabla(jugadoresInterme)
            elif (opMenu == 3):
                jugador.mostrarTabla(jugadoresAvanza)
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")

def menuGanadores():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerGanadores)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                if (len(jugadoresNova) < 5):
                    print(f"No se han registrado el mínimo de jugadores en esta categoría")
                else:
                    partidosRealizados = partido.NumPartidos(len(jugadoresNova))
                    if (partidosRealizados == len(partido.partidosNovatos)):
                        print(f"GANADOR/A NOVATO/A")
                        jugador.mostrarGanador(jugadoresNova)
                    else:
                        print(f"El torneo no ha terminado")
            elif (opMenu == 2):
                if (len(jugadoresInterme) < 5):
                    print(f"No se han registrado el mínimo de jugadores en esta categoría")
                else:
                    partidosRealizados = partido.NumPartidos(len(jugadoresInterme))
                    if (partidosRealizados == len(partido.partidosIntermedios)):
                        print(f"GANADOR/A INTERMDEDIO/A")
                        jugador.mostrarGanador(jugadoresInterme)
                    else:
                        print(f"El torneo no ha terminado")
            elif (opMenu == 3):
                if (len(jugadoresAvanza) < 5):
                    print(f"No se han registrado el mínimo de jugadores en esta categoría")
                else:
                    partidosRealizados = partido.NumPartidos(len(jugadoresAvanza))
                    if (partidosRealizados == len(partido.partidosAvanzados)):
                        print(f"GANADOR/A AVANZADO/A")
                        jugador.mostrarGanador(jugadoresAvanza)
                    else:
                        print(f"El torneo no ha terminado")
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")