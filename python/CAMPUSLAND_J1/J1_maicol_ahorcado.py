import random

print("Bienvenidos al ahorcado")
print("-------------------------------------------")

wordDictionary = ["casa", "python", "años", "memes","yeet","hello", "dinero", "like", "subscribe"]

### Choose a random word
randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end=" ")

def imprimir_ahorcado(incorrecto):
  if(incorrecto == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(incorrecto == 1):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(incorrecto == 2):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(incorrecto == 3):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

def imprimirPalabra(adivinadoCartas):
  contar=0
  derechaCartas=0
  for contador in randomWord:
    if(contador in adivinadoCartas):
      print(randomWord[contar], end=" ")
      derechaCartas+=1
    else:
      print(" ", end=" ")
    contar+=1
  return derechaCartas

def imprimirlíneas():
  print("\r")
  for contador in randomWord:
    print("\u203E", end=" ")

longitud_de_la_palabra_a_adivinar = len(randomWord)
cantidad_de_veces_incorrecta = 0
índice_conjetura_actual = 0
letras_actuales_adivinadas = []
letras_actuales_derecha = 0

while(cantidad_de_veces_incorrecta != 4 and letras_actuales_derecha != longitud_de_la_palabra_a_adivinar):
  print("\nLetras adivinadas hasta el momento ")
  for letra in letras_actuales_adivinadas:
    print(letra, end=" ")
  
  cartaadivinada = input("\nadivina una letra ")
  
  if(randomWord[índice_conjetura_actual] == cartaadivinada):
    imprimir_ahorcado(cantidad_de_veces_incorrecta)
   
    índice_conjetura_actual+=1
    letras_actuales_adivinadas.append(cartaadivinada)
    letras_actuales_derecha = imprimirPalabra(letras_actuales_adivinadas)
    imprimirlíneas()
  
  else:
    cantidad_de_veces_incorrecta+=1
    letras_actuales_adivinadas.append(cartaadivinada)
    
    imprimir_ahorcado(cantidad_de_veces_incorrecta)
    
    letras_actuales_derecha = imprimirPalabra(letras_actuales_adivinadas)
    imprimirlíneas()

print("¡El juego ha terminado! Gracias por jugar:)")