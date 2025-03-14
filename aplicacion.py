import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt

# Colores del cubo
COLORES = {
    "B": QColor("white"),   # Blanco (Arriba)
    "V": QColor("green"),   # Verde (Izquierda)
    "N": QColor("orange"),  # Naranja (Atrás)
    "R": QColor("red"),     # Rojo (Frente)
    "AZ": QColor("blue"),   # Azul (Derecha)
    "AM": QColor("yellow")  # Amarillo (Abajo, no editable)
}

# Posiciones de cada cara
POSICIONES_CARAS = {
    "B": (100, -20),   # Blanco (Arriba)
    "V": (-20, 100),   # Verde (Izquierda)
    "N": (100, 100),   # Naranja (Atrás)
    "R": (220, 100),   # Rojo (Frente)
    "AZ": (340, 100),  # Azul (Derecha)
    "AM": (100, 220)   # Amarillo (Abajo, no editable)
}

# Caras contiguas a la cara blanca (excepto la cara amarilla)
CARAS_CONTIGUAS_BLANCA = ["V", "N", "R", "AZ"]

class CuboTile(QGraphicsRectItem):
    def __init__(self, x, y, size, color, cara, fila, columna):
        super().__init__(x, y, size, size)
        self.setBrush(QBrush(color))
        self.setPen(QPen(Qt.GlobalColor.black, 2))
        self.cara = cara
        self.fila = fila
        self.columna = columna
        self.color_actual = color

    def mousePressEvent(self, event):
        # Cambiar color si es la cara blanca (excepto la casilla central)
        if self.cara == "B" and (self.fila != 1 or self.columna != 1):
            self.cambiar_color()

        # Cambiar color si es una de las casillas en la fila superior de las caras contiguas
        if self.cara in CARAS_CONTIGUAS_BLANCA and self.fila == 0:
            self.cambiar_color()

    def cambiar_color(self):
        # Ciclo de colores
        color_keys = list(COLORES.keys())
        indice_actual = color_keys.index(self.cara)
        # Pasar al siguiente color cíclicamente
        nuevo_color = color_keys[(indice_actual + 1) % len(color_keys)]
        self.color_actual = COLORES[nuevo_color]
        self.setBrush(QBrush(self.color_actual))  # Actualiza el color de la casilla
        self.cara = nuevo_color  # Actualiza la cara para la siguiente iteración


class Cubo3D(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cubo Rubik - Última Capa")
        self.setGeometry(100, 100, 400, 400)
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.casilla_size = 40
        self.crear_cubo()

    def crear_cubo(self):
        for cara, (x, y) in POSICIONES_CARAS.items():
            for fila in range(3):
                for columna in range(3):
                    color_inicial = COLORES[cara]  
                    # Evitar que la casilla central de la cara blanca sea clicable
                    if cara == "B" and fila == 1 and columna == 1:
                        color_inicial = COLORES["B"]  # Mantener el color blanco en el centro
                    tile = CuboTile(
                        x + columna * self.casilla_size, 
                        y + fila * self.casilla_size,
                        self.casilla_size, 
                        color_inicial, cara, fila, columna
                    )
                    self.scene.addItem(tile)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cubo3D()
    window.show()
    sys.exit(app.exec())
