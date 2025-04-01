
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
    def __init__(self, cara, fila, columna, color, molecula_adyacente):
        super().__init__(cara, fila, columna, color)
        self.molecula_adyacente = molecula_adyacente

class Vertice(Arista):
    def __init__(self, cara, fila, columna, color, molecula_adyacente, molecula_precedente):
        super().__init__(cara, fila, columna, color, molecula_adyacente)
        self.molecula_precedente = molecula_precedente

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
        
    
def search(cubo, cara, fila, columna):
    for i in range(3):
        for j in range(3):
            mol = cubo[i][j]
            if isinstance(mol, Molecula):
                print(mol.fila)
                if mol.fila == fila and mol.columna == columna and mol.cara == cara:
                    print(f"Encontrado: {mol.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                
                elif mol.molecula_adyacente.fila == fila and mol.molecula_adyacente.columna == columna and mol.molecula_adyacente.cara == cara:
                    print(f"Encontrado: {mol.molecula_adyacente.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                    
                elif isinstance(mol, Vertice) and mol.molecula_precedente.fila == fila and mol.molecula_precedente.columna == columna and mol.molecula_precedente.cara == cara:
                    print(f"Encontrado: {mol.molecula_precedente.cara} en fila {fila}, columna {columna}, en {i}, {j}")
                
                else:
                    print("No encontrado")
                
    
    
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
    
    search(cubo, "N", 0, 0)
    
    return cubo


iniciar()