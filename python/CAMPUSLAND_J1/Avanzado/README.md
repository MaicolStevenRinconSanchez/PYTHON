Torneo de Tenis de Mesa 
Este proyecto consiste en un sistema para gestionar un torneo de tenis de mesa en un campus. 
Permite registrar jugadores, partidos, y calcular los ganadores en diferentes categorías. A continuación, se detalla la estructura y el funcionamiento del proyecto.

Estructura del Proyecto
main.py: Archivo principal que ejecuta el programa y maneja el menú principal.
jugadores.py: Contiene funciones relacionadas con el registro y la gestión de jugadores.
partidos.py: Contiene funciones para registrar partidos y calcular ganadores.
menus.py: Define los menús y funciones auxiliares para la interacción con el usuario.
categorias.py: Define una función para asignar categorías a jugadores según su edad.
Funcionalidades
Registro de Jugadores:

Permite registrar jugadores en tres categorías: Novato, Intermedio y Avanzado, según su edad.
Almacena información como el código, nombre, edad y categoría del jugador.
Registro de Partidos:

Permite registrar partidos entre jugadores, ingresando los resultados de cada set.
Calcula automáticamente el ganador del partido y actualiza los puntajes de los jugadores.
Tabla de Puntajes:

Muestra la tabla de puntajes para cada categoría, incluyendo el número de partidos jugados, ganados, perdidos, puntos a favor y total de puntos.
Ganadores por Categoría:

Determina y muestra al ganador de cada categoría basándose en el total de puntos acumulados.
Verifica si se ha alcanzado el número mínimo de jugadores para comenzar el torneo.
Uso del Programa
Ejecutar el archivo main.py.
Seleccionar opciones del menú principal para realizar operaciones específicas.
Seguir las instrucciones proporcionadas por el programa.
Consideraciones Importantes
Cada categoría requiere un mínimo de 5 jugadores para iniciar el torneo.
Los resultados de los partidos se registran por sets, y el programa determina automáticamente al ganador del partido.
