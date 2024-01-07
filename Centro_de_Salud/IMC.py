# IMC.py

import os

def salud():
    codigo = int(input("codigo: "))
    nombre = input("nombre: ")
    edad = int(input("edad: "))
    altura = float(input("altura (en metros): "))
    peso = float(input("peso (en kg): "))
    registro = {
        "codigo": codigo,
        "nombre": nombre,
        "edad": edad,
        "altura": altura,
        "peso": peso
    }
    return registro
def imc(codigo,nombre, edad, altura, peso):
    indice_masa_corporal = peso / (altura * altura)
 
    if 18.5 <= indice_masa_corporal <= 24.9:
        estado = "NORMAL"
    elif 25 <= indice_masa_corporal <= 29.9:
        estado = "SOBREPESO"
    elif 30 <= indice_masa_corporal <= 34.9:
        estado = "OBESIDAD I"
    elif 35 <= indice_masa_corporal <= 39.9:
        estado = "OBESIDAD II"
    elif indice_masa_corporal >= 40:
        estado = "OBESIDAD III"
    else:
        estado = "DESNUTRIDO"

    return f"IMC: {indice_masa_corporal:.2f}, Estado: {estado}"

$ git push origin CAMPUSLAND_J1
# Pushes the changes in your local repository up to the remote repository you specified as the origin
