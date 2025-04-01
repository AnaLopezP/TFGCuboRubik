

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
    
class Matriz:
    def __init__(self):
        self.matriz = [
            [Cubito("a", "B", "R"), Cubito("b", "B", "AZ"), Cubito("c", "B", "N")],
            [Cubito("d", "B", "V"), Cubito("e", "B", "R", "AZ"), Cubito("f", "B", "AZ", "N")],
            [Cubito("g", "B", "N", "V"), Cubito("h", "B", "N", "R"), None]
        ]
        