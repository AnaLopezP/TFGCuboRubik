
from grafo import grafo, buscar_nodo, buscar_identidad

# --- en orbitas.py (o justo después de importarlo) ---

# Posición de cada arista en la cara blanca y su posición lateral
net_aristas_blanca = {
    1: (0, 1),
    2: (1, 0),
    3: (2, 1),
    4: (1, 2)
}
net_aristas_lateral = {
    1: ("R", (2, 1)),
    2: ("AZ", (1, 2)),
    3: ("N", (0, 1)),
    4: ("V", (1, 0))
}

# Posición de cada esquina en la cara blanca y sus dos posiciones laterales
net_esquinas_blanca = {
    1: (0, 0),
    2: (2, 0),
    3: (2, 2),
    4: (0, 2)
}
net_esquinas_lateral1 = {
    1: ("R", (2, 0)),
    2: ("AZ", (2, 2)),
    3: ("N", (0, 2)),
    4: ("V", (0, 0))
}
net_esquinas_lateral2 = {
    1: ("AZ", (0, 2)),
    2: ("N",  (0, 0)),
    3: ("V",  (2, 0)),
    4: ("R",  (2, 2))
}


def solucionar_otra_orbita(mov_recibido):
    movimiento_cercano = None
    diferencia_minima = float('inf')
    indice_diferente = None
    tipo_diferente = None  # 'arista' o 'vertice'

    for nodo in grafo.nodos.values():
        mov = nodo.movimiento
        dif = 0
        idx_dif = None
        tipo = None

        # Comparar orientaciones de aristas
        for i, (a, b) in enumerate(zip(mov_recibido[1], mov[1])):
            if a != b:
                dif += 1
                idx_dif = i
                tipo = 'arista'

        # Comparar orientaciones de vértices
        for i, (a, b) in enumerate(zip(mov_recibido[3], mov[3])):
            if a != b:
                dif += 1
                idx_dif = i
                tipo = 'vertice'

        if dif == 1:
            # Encontramos un candidato válido
            movimiento_cercano = mov
            indice_diferente = idx_dif
            tipo_diferente = tipo
            break  # Terminamos la búsqueda al encontrar el primero válido

    if not movimiento_cercano:
        raise ValueError("No se encontró ningún movimiento cercano en el grafo.")

    # Obtener la solución desde el movimiento cercano
    numero_mov = buscar_nodo(movimiento_cercano)
    secuencia, historial = buscar_identidad(numero_mov)

    # Corregimos el historial, cambiando la pieza 'buena' por la 'incorrecta'
    historial_corregido = []
    for num in historial:
        mov = grafo.nodos[num].movimiento
        mov_corregido = list(mov)

        if tipo_diferente == 'arista':
            orientacion = mov_corregido[1][:]
            orientacion[indice_diferente] = mov_recibido[1][indice_diferente]
            mov_corregido[1] = orientacion
        else:
            orientacion = mov_corregido[3][:]
            orientacion[indice_diferente] = mov_recibido[3][indice_diferente]
            mov_corregido[3] = orientacion

        historial_corregido.append(tuple(mov_corregido))

    return secuencia, historial_corregido


def corregir_movimiento(mov_recibido):
    """
    Busca en el grafo el único movimiento que coincide en todo salvo
    en una orientación, y devuelve:
      - mov_can:  el movimiento “canónico” (en tu grafo)
      - tipo:     'arista' o 'vertice'
      - idx:      índice 0..3 de la pieza distinta
    """
    for nodo in grafo.nodos.values():
        mov = nodo.movimiento
        # contamos diferencias en orient_edges y orient_corners
        dif = 0; idx = None; tipo = None
        for i,(a,b) in enumerate(zip(mov_recibido[1], mov[1])):
            if a!=b: dif+=1; idx=i; tipo='arista'
        for i,(a,b) in enumerate(zip(mov_recibido[3], mov[3])):
            if a!=b: dif+=1; idx=i; tipo='vertice'
        if dif==1:
            return mov, tipo, idx
    raise ValueError("No se encontró movimiento cercano")
