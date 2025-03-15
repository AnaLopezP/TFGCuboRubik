import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt


# Colores del cubo
COLORES = ["B", "V", "N", "R", "AZ", "AM"]
COLORES_MAPA = {
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
        self.color_actual = cara

    def mousePressEvent(self, event):
        # Cambiar color si es la cara blanca (excepto la casilla central)
        if self.cara == "B" and not (self.fila == 1 and self.columna == 1):
            self.cambiar_color()
        # Cambiar color si es una cara contigua a la blanca, en la fila 0
        elif self.fila == 0 and self.cara in CARAS_CONTIGUAS_BLANCA:
            self.cambiar_color()
        

    def cambiar_color(self):
        # Ciclo de colores
        indice_actual = COLORES.index(self.color_actual)
        print(f"indice actual: {indice_actual}")
        # Pasar al siguiente color cíclicamente
        nuevo_color = COLORES[(indice_actual + 1) % len(COLORES)]
        print((indice_actual + 1) % len(COLORES))
        print(f"nuevo color: {nuevo_color}")
        self.setBrush(QBrush(COLORES_MAPA[nuevo_color]))  # Actualiza el color de la casilla
        self.color_actual = nuevo_color  # Actualiza la cara para la siguiente iteración


class Cubo3D(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cubo Rubik - Última Capa")
        self.setGeometry(100, 100, 400, 400)
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.casilla_size = 40
        self.modo_perspaectiva = False
        
        self.crear_cubo_plano()

    def crear_cubo_plano(self):
        self.scene.clear()
        for cara, (x, y) in POSICIONES_CARAS.items():
            for fila in range(3):
                for columna in range(3):
                    color_inicial = COLORES_MAPA[cara]  
                    # Evitar que la casilla central de la cara blanca sea clicable
                    if cara == "B" and fila == 1 and columna == 1:
                        color_inicial = COLORES_MAPA["B"]  # Mantener el color blanco en el centro
                    tile = CuboTile(
                        x + columna * self.casilla_size, 
                        y + fila * self.casilla_size,
                        self.casilla_size, 
                        color_inicial, cara, fila, columna
                    )
                    self.scene.addItem(tile)
        
    def crear_cubo_perspectiva(self):
        self.scene.clear()
        # proximamente
        pass
                    
    def cambiar_vista(self):
        self.modo_persepectiva = not self.modo_persepectiva
        if self.modo_persepectiva:
            self.crear_cubo_perspectiva()
        else:
            self.crear_cubo_plano()
            
class Interfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cubo Rubik - Interfaz")
        
        self.layout = QVBoxLayout()
        self.cubo = Cubo3D()
        self.cambiar_vista_btn = QPushButton("Cambiar Vista")
        self.cambiar_vista_btn.clicked.connect(self.cubo.cambiar_vista)
        
        self.layout.addWidget(self.cubo)
        self.layout.addWidget(self.cambiar_vista_btn)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cubo3D()
    window.show()
    sys.exit(app.exec())
