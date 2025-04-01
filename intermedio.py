
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
    
    asignar_color(cubo, "N", 0, 0, "R")
    
    return cubo


iniciar()