# Diccionario de órbitas
ORBITAS = {
    # vertice 0,0
    ((0, 0), 1): 1,
    ((0, 0), 2): 2,
    # arista 0,1
    ((0, 1), 1): 3,
    # vertice 0,2
    ((0, 2), 1): 4,
    ((0, 2), 2): 5,
    # arista 1,0
    ((1, 0), 1): 6,
    # arista 1,2
    ((1, 2), 1): 7,
    # vertice 2,0
    ((2, 0), 1): 8,
    ((2, 0), 2): 9,
    # arista 2,1
    ((2, 1), 1): 10,
    # vertice 2,2
    ((2, 2), 1): 11,
    ((2, 2), 2): 12,
}

EDGE_POS   = [(0,1), (1,0), (2,1), (1,2)]
CORNER_POS = [(0,0), (2,0), (2,2), (0,2)]

def restricciones_orientaciones(orient_edges, orient_corners):
    """
    Devuelve True si:
      - sum(orient_edges) % 2 == 0
      - sum(orient_corners) % 3 == 0
    False en caso contrario.
    """
    ok_aristas  = (sum(orient_edges) % 2 == 0)
    ok_esquinas = (sum(orient_corners) % 3 == 0)
    return ok_aristas and ok_esquinas

def detectar_orbita_desde_movimiento(movimiento):
    perm_edges, orient_edges, perm_corners, orient_corners = movimiento
    
    # 1) Si está en órbita canónica, no hace falta más
    if restricciones_orientaciones(orient_edges, orient_corners):
        return 0  # órbita canónica

    # 2) Si la suma de aristas no cuadra, buscamos qué arista está “flippeada”
    if sum(orient_edges) % 2 != 0:
        for idx, o in enumerate(orient_edges):
            if o != 0:
                pos = EDGE_POS[idx]
                return identificar_orbita(pos, o)

    # 3) Si la suma de esquinas no cuadra, buscamos qué esquina está mal girada
    if sum(orient_corners) % 3 != 0:
        for idx, o in enumerate(orient_corners):
            if o != 0:
                pos = CORNER_POS[idx]
                return identificar_orbita(pos, o)

    # En caso extraño (oriento sumas mal pero no encuentro pieza), devolvemos None
    return None

def identificar_orbita(posicion, orientacion):
    """
    Dada una posición (por ejemplo, (fila, columna)) y la orientación
    (por ejemplo, 1 o 2 para las piezas mal puestas), devuelve el número de órbita.
    Si la pieza estuviese en estado canónico se devolverá 0 (o None).
    """
    # Suponiendo que en el estado canónico la orientación sea 0 (y no esté en el diccionario)
    return ORBITAS.get((posicion, orientacion), 0)

def calcular_transformacion(orbita_actual, orbita_canonica=0):
    """
    Dada la órbita de la pieza (por ejemplo, 3, 5, etc.) y la órbita canónica (usualmente 0),
    retorna una transformación g que corrija la diferencia.
    En este ejemplo se retorna una "transformación" dummy, representada como una lista de movimientos.
    """
    if orbita_actual == orbita_canonica:
        return []  # Identidad
    # Para ilustrar: supondremos que la transformación es simplemente un "flip"
    # La cantidad de "flip" o el contenido dependerá de la diferencia.
    diferencia = orbita_actual - orbita_canonica
    # Por ejemplo, cada unidad de diferencia se corrige con un "flip"
    return ["flip"] * abs(diferencia)

def inversa(transf):
    """
    Calcula la transformación inversa.
    Asumimos que "flip" es involutiva (flip = flip), así que la inversa es la misma secuencia, invertida.
    """
    return transf[::-1]

def concatenar(*listas):
    """Concatena varias listas de movimientos"""
    resultado = []
    for L in listas:
        resultado += L
    return resultado

def aplicar_conjugacion_movimiento(movimiento, g):
    """
    Dada una secuencia de movimiento y una transformación g,
    retorna: g + movimiento + g^-1
    """
    return concatenar(g, movimiento, inversa(g))
