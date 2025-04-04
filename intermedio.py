from estado_cubo import cube_state
from main import *
class Molecula:
    def __init__(self):
        self.cara = None
        self.fila = None
        self.columna = None
        self.color = None
        
    def set_color(self, color):
        self.color = color
        
    
        
    def __init__(self, cara, fila, columna, color):
        self.cara = cara
        self.fila = fila
        self.columna = columna
        self.color = color

class Arista(Molecula):
    def __init__(self, cara, fila, columna, color, adyacente):
        super().__init__(cara, fila, columna, color)
        self.adyacente = adyacente

class Vertice(Arista):
    def __init__(self, cara, fila, columna, color, adyacente, precedente):
        super().__init__(cara, fila, columna, color, adyacente)
        self.precedente = precedente


    
def asignar_color(cubo, cara, fila, columna, nuevo_color):
    cube_state[cara][fila][columna] = nuevo_color
    #print(f"Color asignado a {cara} en fila {fila}, columna {columna}: {nuevo_color}")
    
    for i in range(3):
        for j in range(3):
            mol = cubo[i][j]
            if isinstance(mol, Molecula):
                #print(mol.fila)
                if mol.fila == fila and mol.columna == columna and mol.cara == cara:
                    #print(f"Encontrado: {mol.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    mol.set_color(nuevo_color)
                
                elif mol.adyacente.fila == fila and mol.adyacente.columna == columna and mol.adyacente.cara == cara:
                    #print(f"Encontrado: {mol.adyacente.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    mol.adyacente.set_color(nuevo_color)
                    
                elif isinstance(mol, Vertice) and mol.precedente.fila == fila and mol.precedente.columna == columna and mol.precedente.cara == cara:
                    #print(f"Encontrado: {mol.precedente.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    mol.precedente.set_color(nuevo_color)
                
                else:
                    print("No encontrado")
    #print("Color asignado correctamente")   
    
def iniciar():
    cubo = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    cubo[0][0] = Vertice("B", 0, 0, "B", Molecula("R", 2, 0, "R"), Molecula("AZ", 0, 2, "AZ"))
    cubo[0][1] = Arista("B", 0, 1, "B", Molecula("R", 2, 1, "R"))
    cubo[0][2] = Vertice("B", 0, 2, "B", Molecula("V", 0, 0, "V"), Molecula("R", 2, 2, "R"))
    cubo[1][0] = Arista("B", 1, 0, "B", Molecula("AZ", 1, 2, "AZ"))
    cubo[1][1] = None
    cubo[1][2] = Arista("B", 1, 2, "B", Molecula("V", 1, 0, "V"))
    cubo[2][0] = Vertice("B", 2, 0, "B", Molecula("AZ", 2, 2, "AZ"), Molecula("N", 0, 0, "N"))
    cubo[2][1] = Arista("B", 2, 1, "B", Molecula("N", 0, 1, "N"))
    cubo[2][2] = Vertice("B", 2, 2, "B", Molecula("N", 0, 2, "N"), Molecula("V", 2, 0, "V"))
    
    return cubo


def indice_arista_resuelta(pieza):
    # Se detecta cuál de las dos pegatinas es la blanca y se toma la otra
    if pieza.color == "B":
        otro = pieza.adyacente.color
    elif pieza.adyacente.color == "B":
        otro = pieza.color
    else:
        raise ValueError(f"Arista sin pegatina blanca: {pieza}")
    
    mapping_aristas = {
        "R": 1,
        "AZ": 2,
        "N": 3,
        "V": 4
    }
    
    pos_resuelta = mapping_aristas.get(otro)
    
    if pos_resuelta is None:
        raise ValueError(f"Combinación ('B', '{otro}') no definida para aristas.")
    return pos_resuelta
    
def indice_esquina_resuelta(pieza):
    if pieza.color == "B":
        otros = {pieza.adyacente.color, pieza.precedente.color}
    elif pieza.adyacente.color == "B":
        otros = {pieza.color, pieza.precedente.color}
    elif pieza.precedente.color == "B":
        otros = {pieza.color, pieza.adyacente.color}
    else:
        raise ValueError(f"Esquina sin pegatina blanca: {pieza}")
    
    mapping_esquinas = {
        frozenset({"R", "AZ"}): 1,
        frozenset({"AZ", "N"}): 2,
        frozenset({"N", "V"}): 3,
        frozenset({"V", "R"}): 4
    }
    
    pos_resuelta = mapping_esquinas.get(frozenset(otros))
    if pos_resuelta is None:
        raise ValueError(f"Combinación ('B', {otros}) no definida para esquinas.")
    return pos_resuelta
        
def traducir_a_mov(cubo):
    
    # Mapeo de la posición actual (en la matriz) para las aristas y esquinas
    aristas_pos_actual = {
        (0, 1): 1,  # arriba
        (1, 0): 2,  # izquierda
        (2, 1): 3,  # derecha
        (1, 2): 4   # abajo
    }

    esquinas_pos_actual = {
        (0, 0): 1,  # arriba izquierda
        (2, 0): 2,  # abajo izquierda
        (2, 2): 3,  # abajo derecha
        (0, 2): 4   # arriba derecha
    }
    
    permutación_aristas = {}
    permutación_esquinas = {}

    # PRIMER PASO: Registrar la permutación de las piezas**  
    for i in range(3):
        for j in range(3):
            pieza = cubo[i][j]
            if isinstance(pieza, Molecula):
                pos_actual = (i, j)
                
                # Caso: Arista
                if pos_actual in aristas_pos_actual:
                    indice_actual = aristas_pos_actual[pos_actual]
                    resuelto = indice_arista_resuelta(pieza)
                    permutación_aristas[resuelto] = indice_actual
                
                # Caso: Esquina
                elif pos_actual in esquinas_pos_actual:
                    indice_actual = esquinas_pos_actual[pos_actual]
                    resuelto = indice_esquina_resuelta(pieza)
                    permutación_esquinas[resuelto] = indice_actual
    
    # SEGUNDO PASO: Asignar la orientación correctamente según la posición rotada**
    orientacion_aristas = [None] * 4
    orientacion_esquinas = [None] * 4

    for resuelto, indice_actual in permutación_aristas.items():
        pos_actual = next(k for k, v in aristas_pos_actual.items() if v == indice_actual)
        pieza = cubo[pos_actual[0]][pos_actual[1]]
        
        if pieza.color == "B":
            orientacion_aristas[indice_actual - 1] = 0
        elif pieza.adyacente.color == "B":
            orientacion_aristas[indice_actual - 1] = 1
        else:
            print(f"Error: arista {indice_actual} sin pegatina blanca en ninguna posición.")

    for resuelto, indice_actual in permutación_esquinas.items():
        pos_actual = next(k for k, v in esquinas_pos_actual.items() if v == indice_actual)
        pieza = cubo[pos_actual[0]][pos_actual[1]]
        
        if pieza.color == "B":
            orientacion_esquinas[indice_actual - 1] = 0
        elif pieza.adyacente.color == "B":
            orientacion_esquinas[indice_actual - 1] = 1
        elif pieza.precedente.color == "B":
            orientacion_esquinas[indice_actual - 1] = 2
        else:
            print(f"Error: esquina {indice_actual} sin pegatina blanca en ninguna posición.")

    # Ordenamos los diccionarios por clave para mantener un orden coherente
    permutación_aristas = dict(sorted(permutación_aristas.items()))
    permutación_esquinas = dict(sorted(permutación_esquinas.items()))
    
    return [permutación_aristas, orientacion_aristas, permutación_esquinas, orientacion_esquinas]

def traducir_a_cubo(movimiento, cube_state):
   # Si el movimiento es un str, buscamos en el grafo el nodo que tenga ese nombre
    if isinstance(movimiento, str):
        # Se asume que 'grafo' está importado y es la instancia global del grafo
        encontrado = False
        for nodo in grafo.nodos.values():
            if nodo.nombre == movimiento:
                movimiento = nodo.movimiento
                encontrado = True
                print(f"Movimiento encontrado en el grafo: {nodo.nombre} -> {movimiento}")
                break
        if not encontrado:
            raise ValueError(f"No se encontró movimiento en el grafo para el nombre: {movimiento}")

    # --- ARISTAS ---
    # Para las aristas consideramos:
    #   1: blanco-rojo, 2: blanco-azul, 3: blanco-naranja, 4: blanco-verde
    # Las posiciones en la cara blanca (B) se definen así (fila, columna):
    aristas_blanca = {
        1: (0, 1),  # arriba
        2: (1, 0),  # izquierda
        3: (2, 1),  # abajo
        4: (1, 2)   # derecha
    }
    # Para cada arista, definimos también la posición en la cara lateral (según su color)
    # (Estos valores dependen de cómo se dispongan las caras en tu net)
    aristas_lateral = {
        1: ("R", (2, 1)),   # para blanco-rojo, en la cara roja
        2: ("AZ", (1, 2)),  # para blanco-azul, en la cara azul
        3: ("N", (0, 1)),   # para blanco-naranja, en la cara naranja
        4: ("V", (1, 0))    # para blanco-verde, en la cara verde
    }
    print(movimiento)
    # Procesamos cada arista (1 a 4)
    for num in [1, 2, 3, 4]:
        # Obtenemos la nueva posición (entre 1 y 4) para esta pieza según el movimiento
        nueva_pos = movimiento[0][num]  
        # La orientación se determina mirando el elemento de la lista de orientaciones
        orientacion = movimiento[1][nueva_pos-1]
        
        # Según la orientación, se asigna la pegatina blanca a la cara blanca o a la lateral
        if orientacion == 0:
            # Pegatina blanca en la cara blanca
            cara_blanca, pos_blanca = "B", aristas_blanca[num]
            cara_lateral, pos_lateral = aristas_lateral[num]
        elif orientacion == 1:
            # Pegatina blanca se traslada a la cara lateral
            cara_blanca, pos_blanca = "B", aristas_blanca[num]
            cara_lateral, pos_lateral = aristas_lateral[num]
            # En este caso, invertimos: la pegatina blanca se pone en la lateral y el otro color
            # se asigna a la blanca. (Asumimos que “B” es la letra del blanco y la otra ya viene en el mapping)
            # Para efectos de este ejemplo, simplemente intercambiamos el rol de la pegatina.
            cara_blanca, cara_lateral = cara_lateral, cara_blanca
        else:
            raise ValueError(f"Orientación desconocida en arista {num}: {orientacion}")

        # Actualizamos el estado en la cara blanca: se coloca la pegatina blanca ("B")
        fila, col = pos_blanca
        print(f"Actualizando cara blanca: {fila}, {col} con {cara_blanca}")
        cube_state[cara_blanca][fila][col] = "B"
        # Actualizamos la cara lateral: se coloca el color de la pieza (la que no es blanca)
        fila, col = pos_lateral
        # Se usa la letra de la cara lateral (p.ej. "R", "AZ", "N" o "V")
        print(f"Actualizando cara lateral: {fila}, {col} con {cara_lateral}")
        cube_state[cara_lateral][fila][col] = cara_lateral

    # --- ESQUINAS ---
    # Definimos las posiciones de la pegatina blanca en la cara blanca para cada esquina.
    esquinas_blanca = {
        1: (0, 0),  # esquina superior izquierda en B
        2: (2, 0),  # esquina inferior izquierda en B
        3: (2, 2),  # esquina inferior derecha en B
        4: (0, 2)   # esquina superior derecha en B
    }
    # Definimos la posición de la primera pegatina lateral para cada esquina.
    esquinas_lateral1 = {
        1: ("R", (2, 0)),  # para la esquina 1, la pegatina roja en R
        2: ("AZ", (2, 2)), # para la esquina 2, la pegatina azul en AZ
        3: ("N", (0, 2)),  # para la esquina 3, la pegatina naranja en N
        4: ("V", (0, 0))   # para la esquina 4, la pegatina verde en V
    }
    # Definimos la posición de la segunda pegatina lateral para cada esquina.
    esquinas_lateral2 = {
        1: ("AZ", (0, 2)),  # para la esquina 1, la pegatina azul en AZ
        2: ("N", (0, 0)),   # para la esquina 2, la pegatina naranja en N
        3: ("V", (2, 0)),   # para la esquina 3, la pegatina verde en V
        4: ("R", (2, 2))    # para la esquina 4, la pegatina roja en R
    }

    # Para cada esquina (1 a 4)
    for num in [1, 2, 3, 4]:
        nueva_pos = movimiento[2][num]  # nueva posición (entre 1 y 4)
        orientacion = movimiento[3][nueva_pos - 1]  # orientación: 0, 1 o 2

        if orientacion == 0:
            # Pegatina blanca se queda en B.
            cara_blanca, pos_blanca = "B", esquinas_blanca[num]
            cara_lateral1, pos_lateral1 = esquinas_lateral1[num]
            cara_lateral2, pos_lateral2 = esquinas_lateral2[num]
        elif orientacion == 1:
            # La pegatina blanca se traslada a la primera lateral.
            # La cara B pasará a ser la lateral1, lateral1 pasa a lateral2 y lateral2 pasa a B
            cara_blanca, pos_blanca = esquinas_lateral1[num][0], esquinas_lateral1[num][1]
            cara_lateral1, pos_lateral1 = "B", esquinas_blanca[num]
            cara_lateral2, pos_lateral2 = esquinas_lateral2[num]
        elif orientacion == 2:
            # La pegatina blanca se traslada a la segunda lateral.
            # La cara B pasará a ser la lateral2, lateral2 pasa a lateral1 y lateral1 pasa a B
            cara_blanca, pos_blanca = esquinas_lateral2[num][0], esquinas_lateral2[num][1]
            cara_lateral1, pos_lateral1 = esquinas_lateral1[num]
            cara_lateral2, pos_lateral2 = "B", esquinas_blanca[num]
        else:
            raise ValueError(f"Orientación desconocida en esquina {num}: {orientacion}")

        # Actualizamos la cara que recibe el blanco
        fila, col = pos_blanca
        print(f"Actualizando cara blanca: {fila}, {col} con {cara_blanca}")
        cube_state[cara_blanca][fila][col] = "B"
        # Actualizamos las otras dos caras con los colores correspondientes
        fila, col = pos_lateral1
        cube_state[cara_lateral1][fila][col] = cara_lateral1
        print(f"Actualizando cara lateral1: {fila}, {col} con {cara_lateral1}")
        fila, col = pos_lateral2
        cube_state[cara_lateral2][fila][col] = cara_lateral2
        print(f"Actualizando cara lateral2: {fila}, {col} con {cara_lateral2}")

    print("cube_state actualizado:")
    for cara, matriz in cube_state.items():
        print(cara, matriz)

    return cube_state

    
    
    

cubo = iniciar()  # función que inicializa el cubo
movimiento = traducir_a_mov(cubo)
print("Movimiento traducido:")
print(movimiento)

instrucciones = {
    "b1": "Gira la cara blanca 1 vez.",
    
    "g1b2g3b2g3a1g1a3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara roja 3 veces.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara roja 1 vez.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3b2g1b2g1v3g3v1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara roja 1 vez.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara roja 3 veces.\n"
        "8. Gira la cara verde 1 vez."
    ),
    
    "g1b1g3b3g3a1g1a3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara roja 3 veces.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara roja 1 vez.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3b3g1b1g1v3g3v1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara roja 1 vez.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara roja 3 veces.\n"
        "8. Gira la cara verde 1 vez."
    ),
    
    "a1b2a3b2a3n1a1n3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara azul 3 veces.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara azul 1 vez.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3b2a1b2a1g3a3g1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara azul 1 vez.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara azul 3 veces.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "a1b1a3b3a3n1a1n3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara azul 3 veces.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara azul 1 vez.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3b3a1b1a1g3a3g1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara azul 1 vez.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara azul 3 veces.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "n1b2n3b2n3v1n1v3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara naranja 3 veces.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara naranja 1 vez.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3b2n1b2n1a3n3a1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara naranja 1 vez.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara naranja 3 veces.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "n1b1n3b3n3v1n1v3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara naranja 3 veces.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara naranja 1 vez.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3b3n1b1n1a3n3a1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara naranja 1 vez.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara naranja 3 veces.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "v1b2v3b2v3g1v1g3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara verde 3 veces.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara verde 1 vez.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3b2v1b2v1n3v3n1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara verde 1 vez.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara verde 3 veces.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "v1b1v3b3v3g1v1g3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara verde 3 veces.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara verde 1 vez.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3b3v1b1v1n3v3n1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara verde 1 vez.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara verde 3 veces.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "b3": "Gira la cara blanca 3 veces.",
    
    "a1g3a3g1b2g1b2g3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara roja 3 veces.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara roja 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3g1v1g3b2g3b2g1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara roja 1 vez.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara roja 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "a1g3a3g1b1g1b3g3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara roja 3 veces.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara roja 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3g1v1g3b3g3b1g1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara roja 1 vez.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara roja 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "n1a3n3a1b2a1b2a3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara azul 3 veces.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara azul 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3a1g1a3b2a3b2a1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara azul 1 vez.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara azul 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "n1a3n3a1b1a1b3a3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara azul 3 veces.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara azul 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3a1g1a3b3a3b1a1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara azul 1 vez.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara azul 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "v1n3v3n1b2n1b2n3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara naranja 3 veces.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara naranja 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3n1a1n3b2n3b2n1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara naranja 1 vez.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara naranja 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "v1n3v3n1b1n1b3n3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara naranja 3 veces.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara naranja 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3n1a1n3b3n3b1n1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara naranja 1 vez.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara naranja 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "g1v3g3v1b2v1b2v3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara verde 3 veces.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara verde 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3v1n1v3b2v3b2v1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara verde 1 vez.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara verde 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara verde 1 vez."
    ),
    
    "g1v3g3v1b1v1b3v3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara verde 3 veces.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara verde 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3v1n1v3b3v3b1v1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara verde 1 vez.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara verde 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara verde 1 vez."
    )
}
