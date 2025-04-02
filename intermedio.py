
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

class Cubito:
    def __init__(self, nombre, color1, color2, color3 = None, fila = None, columna = None):
        self.nombre = nombre # a, b, c, d aristas; e, f, g, h vertices
        self.color1 = color1 # blanco porque es la cara blanca
        self.color2 = color2 # color de la cara adyacente
        self.color3 = color3 # color de la otra cara adyacente (si es una esquina)
        self.fila = fila
        self.columna = columna 
        
    def __str__(self):
        return f" Cubito: (Nombre: {self.nombre}, Color1: {self.color1}, Color2: {self.color2}, Color3: {self.color3})"
    
    # para saber en que nueva posición estan los cubitos, buscamos la cara en la que está el color 1 o 2 
    # si el blanco está en la cara blanca, buscamos en qué cara está el color 2
    def buscar_cara(self):
        pass
    
class Matriz:
    def __init__(self):
        self.matriz = [
            [Cubito("a", "B", "R"), Cubito("b", "B", "AZ"), Cubito("c", "B", "N")],
            [Cubito("d", "B", "V"), Cubito("e", "B", "R", "AZ"), Cubito("f", "B", "AZ", "N")],
            [Cubito("g", "B", "N", "V"), Cubito("h", "B", "N", "R"), None]
        ]
        
    
def asignar_color(cubo, cara, fila, columna, nuevo_color):
    for i in range(3):
        for j in range(3):
            mol = cubo[i][j]
            if isinstance(mol, Molecula):
                print(mol.fila)
                if mol.fila == fila and mol.columna == columna and mol.cara == cara:
                    print(f"Encontrado: {mol.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    mol.set_color(nuevo_color)
                
                elif mol.adyacente.fila == fila and mol.adyacente.columna == columna and mol.adyacente.cara == cara:
                    print(f"Encontrado: {mol.adyacente.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    mol.adyacente.set_color(nuevo_color)
                    
                elif isinstance(mol, Vertice) and mol.precedente.fila == fila and mol.precedente.columna == columna and mol.precedente.cara == cara:
                    print(f"Encontrado: {mol.precedente.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    mol.precedente.set_color(nuevo_color)
                
                else:
                    print("No encontrado")
    print("Color asignado correctamente")   
    
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
    cubo[1][2] = Arista("B", 1, 2, "B", Molecula("V", 1, 1, "V"))
    cubo[2][0] = Vertice("B", 2, 0, "B", Molecula("AZ", 2, 2, "AZ"), Molecula("N", 0, 0, "N"))
    cubo[2][1] = Arista("B", 2, 1, "B", Molecula("N", 0, 1, "N"))
    cubo[2][2] = Vertice("B", 2, 2, "B", Molecula("N", 0, 2, "N"), Molecula("V", 2, 0, "V"))
    
    return cubo


def traducir_a_mov(cubo):
    movimiento = [{1:0, 2:0, 3:0, 4:0}, [0, 0, 0, 0], {1:0, 2:0, 3:0, 4:0}, [0, 0, 0, 0]]
    # ---- ARISTAS ----
    # 1. Posición en la permutación
    color_secundario1 = cubo[0][1].adyacente.color
    if color_secundario1 == "R":
        movimiento[0][1] = 1
    elif color_secundario1 == "AZ":
        movimiento[0][1] = 2
    elif color_secundario1 == "N":
        movimiento[0][1] = 3
    elif color_secundario1 == "V":
        movimiento[0][1] = 4
    color_secundario2 = cubo[1][0].adyacente.color
    if color_secundario2 == "R":
        movimiento[0][2] = 1
    elif color_secundario2 == "AZ":
        movimiento[0][2] = 2
    elif color_secundario2 == "N":
        movimiento[0][2] = 3
    elif color_secundario2 == "V":
        movimiento[0][2] = 4
    color_secundario3 = cubo[2][1].adyacente.color
    if color_secundario3 == "R":
        movimiento[0][3] = 1
    elif color_secundario3 == "AZ":
        movimiento[0][3] = 2
    elif color_secundario3 == "N":
        movimiento[0][3] = 3
    elif color_secundario3 == "V":
        movimiento[0][3] = 4
    color_secundario4 = cubo[1][2].adyacente.color
    if color_secundario4 == "R":
        movimiento[0][4] = 1
    elif color_secundario4 == "AZ":
        movimiento[0][4] = 2
    elif color_secundario4 == "N":
        movimiento[0][4] = 3
    elif color_secundario4 == "V":
        movimiento[0][4] = 4
    # 2. Color en la cara blanca

    cara_blancoA = cubo[0][1].cara
    cara_blancoB = cubo[1][0].cara
    cara_blancoC = cubo[2][1].cara
    cara_blancoD = cubo[1][2].cara
    if cara_blancoA == "B":
        movimiento[1][0] = 0
    elif cara_blancoA == "R":
        movimiento[1][0] = 1
    
    if cara_blancoB == "B":
        movimiento[1][1] = 0
    elif cara_blancoB == "AZ":
        movimiento[1][1] = 1
    
    if cara_blancoC == "B":
        movimiento[1][2] = 0
    elif cara_blancoC == "N":
        movimiento[1][2] = 1
    
    if cara_blancoD == "B":
        movimiento[1][3] = 0
    elif cara_blancoD == "V":
        movimiento[1][3] = 1

    
    # ---- VERTICES ----
    # 1. Posición en la permutación
    color_adyacente1 = cubo[0][0].adyacente.color
    color_precedente1 = cubo[0][0].precedente.color
    if color_adyacente1 == "R" and color_precedente1 == "AZ":
        movimiento[2][1] = 1
    elif color_adyacente1 == "AZ" and color_precedente1 == "N":
        movimiento[2][1] = 2
    elif color_adyacente1 == "N" and color_precedente1 == "V":
        movimiento[2][1] = 3
    elif color_adyacente1 == "V" and color_precedente1 == "R":
        movimiento[2][1] = 4
    color_adyacente2 = cubo[2][0].adyacente.color
    color_precedente2 = cubo[2][0].precedente.color
    if color_adyacente2 == "R" and color_precedente2 == "AZ":
        movimiento[2][2] = 1
    elif color_adyacente2 == "AZ" and color_precedente2 == "N":
        movimiento[2][2] = 2
    elif color_adyacente2 == "N" and color_precedente2 == "V":
        movimiento[2][2] = 3
    elif color_adyacente2 == "V" and color_precedente2 == "R":
        movimiento[2][2] = 4
    color_adyacente3 = cubo[0][2].adyacente.color
    color_precedente3 = cubo[0][2].precedente.color
    if color_adyacente3 == "R" and color_precedente3 == "AZ":
        movimiento[2][3] = 1
    elif color_adyacente3 == "AZ" and color_precedente3 == "N":
        movimiento[2][3] = 2
    elif color_adyacente3 == "N" and color_precedente3 == "V":
        movimiento[2][3] = 3
    elif color_adyacente3 == "V" and color_precedente3 == "R":
        movimiento[2][3] = 4
    color_adyacente4 = cubo[2][2].adyacente.color
    color_precedente4 = cubo[2][2].precedente.color
    if color_adyacente4 == "R" and color_precedente4 == "AZ":
        movimiento[2][4] = 1
    elif color_adyacente4 == "AZ" and color_precedente4 == "N":
        movimiento[2][4] = 2
    elif color_adyacente4 == "N" and color_precedente4 == "V":
        movimiento[2][4] = 3
    elif color_adyacente4 == "V" and color_precedente4 == "R":
        movimiento[2][4] = 4
    
    # 2. Color en la cara blanca
    cara_blanco1 = cubo[0][0].cara
    cara_blanco2 = cubo[2][0].cara
    cara_blanco3 = cubo[2][2].cara
    cara_blanco4 = cubo[0][2].cara
    if cara_blanco1 == "B":
        movimiento[3][0] = 0
    elif cara_blanco1 == "R":
        movimiento[3][0] = 1
    elif cara_blanco1 == "AZ":
        movimiento[3][0] = 2
    
    if cara_blanco2 == "B":
        movimiento[3][1] = 0
    elif cara_blanco2 == "AZ":
        movimiento[3][1] = 1
    elif cara_blanco2 == "N":
        movimiento[3][1] = 2
    
    if cara_blanco3 == "B":
        movimiento[3][2] = 0
    elif cara_blanco3 == "N":
        movimiento[3][2] = 1
    elif cara_blanco3 == "V":
        movimiento[3][2] = 2
    
    if cara_blanco4 == "B":
        movimiento[3][3] = 0
    elif cara_blanco4 == "V":
        movimiento[3][3] = 1
    elif cara_blanco4 == "R":
        movimiento[3][3] = 2
    
    return movimiento

# Ejemplo de uso
cubo = iniciar()
mov = traducir_a_mov(cubo)
print(mov)
        
