

class Pegatina:
    def __init__(self, nombre, color1, color2, color3 = None, fila = None, columna = None):
        self.nombre = nombre # a, b, c, d aristas; e, f, g, h vertices
        self.color1 = color1 # blanco porque es la cara blanca
        self.color2 = color2 # color de la cara adyacente
        self.color3 = color3 # color de la otra cara adyacente (si es una esquina)
        self.fila = fila
        self.columna = columna 