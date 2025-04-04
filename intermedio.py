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
    """
    Aplica un movimiento al cubo actualizando el cube_state.
    
    El movimiento es una lista de 4 elementos:
      [
         {1: letra, 2: letra, 3: letra, 4: letra},   # Permutación de aristas (valores: "a", "b", "c", "d")
         [n, n, n, n],                              # Orientaciones de aristas (0 o 1) para posiciones 1..4
         {1: letra, 2: letra, 3: letra, 4: letra},   # Permutación de esquinas (valores: "e", "f", "g", "h")
         [m, m, m, m]                               # Orientaciones de esquinas (0, 1 o 2) para posiciones 1..4
      ]
    
    Se asume que:
      - La cara blanca se denota "B".
      - Las caras laterales se denotan "R", "AZ", "N" y "V".
      - El cube_state es un diccionario de la forma:
            {"B": matriz, "R": matriz, "AZ": matriz, "N": matriz, "V": matriz, ...}
        donde cada matriz es una lista de listas (filas, columnas).
    """
    # --- Preparación y mapeos ---
    # Extraemos los elementos del movimiento:
    edge_perm = movimiento[0]       # Diccionario para aristas; ej: {1:"a", 2:"b", 3:"c", 4:"d"}
    orient_edges = movimiento[1]    # Lista de orientaciones para aristas, en orden para posiciones destino 1..4
    corner_perm = movimiento[2]     # Diccionario para esquinas; ej: {1:"e", 2:"f", 3:"g", 4:"h"}
    orient_corners = movimiento[3]  # Lista de orientaciones para esquinas, para posiciones destino 1..4
    
    # Mapeo de letra a posición destino para aristas y esquinas:
    edge_perm_mapping = {"a": 1, "b": 2, "c": 3, "d": 4}
    corner_perm_mapping = {"e": 1, "f": 2, "g": 3, "h": 4}
    
    # Mapeos de la net para aristas:
    net_aristas_blanca = {1: (0, 1), 2: (1, 0), 3: (2, 1), 4: (1, 2)}
    net_aristas_lateral = {
        1: ("R", (2, 1)),
        2: ("AZ", (1, 2)),
        3: ("N", (0, 1)),
        4: ("V", (1, 0))
    }
    # Colores laterales intrínsecos de las aristas (según la pieza original):
    edge_colors = {1: "R", 2: "AZ", 3: "N", 4: "V"}
    
    # Mapeos de la net para esquinas:
    net_esquinas_blanca = {1: (0, 0), 2: (2, 0), 3: (2, 2), 4: (0, 2)}
    net_esquinas_lateral1 = {
        1: ("R", (2, 0)),
        2: ("AZ", (2, 2)),
        3: ("N", (0, 2)),
        4: ("V", (0, 0))
    }
    net_esquinas_lateral2 = {
        1: ("AZ", (0, 2)),
        2: ("N", (0, 0)),
        3: ("V", (2, 0)),
        4: ("R", (2, 2))
    }
    # Colores laterales intrínsecos de las esquinas (según la pieza original):
    # (orden: (pegatina lateral1, pegatina lateral2))
    corner_colors = {
        1: ("R", "AZ"),
        2: ("AZ", "N"),
        3: ("N", "V"),
        4: ("V", "R")
    }
    
    # --- Procesar aristas ---
    for orig in [1, 2, 3, 4]:
        # Obtenemos la posición destino para la arista que viene de la posición original "orig"
        new_pos = edge_perm_mapping[ edge_perm[orig] ]
        # La orientación se determina para la posición destino (índice new_pos-1)
        orient = orient_edges[new_pos - 1]
        
        # Consultamos las posiciones en la net destino:
        pos_white = net_aristas_blanca[new_pos]     # Ubicación en la cara blanca
        lateral_face_net, pos_lateral = net_aristas_lateral[new_pos]  # Ubicación en la lateral (según la net)
        
        # El color lateral que lleva la pieza (según su posición original):
        inherent_color = edge_colors[orig]
        
        if orient == 0:
            # La pegatina blanca se queda en la cara blanca.
            r, c = pos_white
            cube_state["B"][r][c] = "B"
            r, c = pos_lateral
            cube_state[lateral_face_net][r][c] = inherent_color
        elif orient == 1:
            # Se invierten: la cara blanca recibe el color lateral de la pieza,
            # y en la lateral se coloca la pegatina blanca.
            r, c = pos_white
            cube_state["B"][r][c] = inherent_color
            r, c = pos_lateral
            cube_state[lateral_face_net][r][c] = "B"
        else:
            raise ValueError("Orientación de arista desconocida: " + str(orient))
    
    # --- Procesar esquinas ---
    for orig in [1, 2, 3, 4]:
        new_pos = corner_perm_mapping[ corner_perm[orig] ]
        orient = orient_corners[new_pos - 1]
        
        pos_white = net_esquinas_blanca[new_pos]
        net_face1, pos1 = net_esquinas_lateral1[new_pos]
        net_face2, pos2 = net_esquinas_lateral2[new_pos]
        
        # Los colores laterales originales de la pieza (dependen de la posición original de la esquina)
        inherent_face1, inherent_face2 = corner_colors[orig]
        
        if orient == 0:
            # La pegatina blanca queda en la cara blanca; las laterales conservan sus colores.
            r, c = pos_white
            cube_state["B"][r][c] = "B"
            r, c = pos1
            cube_state[net_face1][r][c] = inherent_face1
            r, c = pos2
            cube_state[net_face2][r][c] = inherent_face2
        elif orient == 1:
            # La pegatina blanca rota hacia la izquierda:
            # En la cara blanca se coloca el color que originalmente estaba en lateral1,
            # y en lateral1 se coloca "B".
            r, c = pos_white
            cube_state["B"][r][c] = inherent_face1
            r, c = pos1
            cube_state[net_face1][r][c] = "B"
            r, c = pos2
            cube_state[net_face2][r][c] = inherent_face2
        elif orient == 2:
            # La pegatina blanca rota hacia la derecha:
            # En la cara blanca se coloca el color que originalmente estaba en lateral2,
            # y en lateral2 se coloca "B".
            r, c = pos_white
            cube_state["B"][r][c] = inherent_face2
            r, c = pos2
            cube_state[net_face2][r][c] = "B"
            r, c = pos1
            cube_state[net_face1][r][c] = inherent_face1
        else:
            raise ValueError("Orientación de esquina desconocida: " + str(orient))
    
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
