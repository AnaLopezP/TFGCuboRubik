import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


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

CUBO_CARAS = {
    "B": [(1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0)],  # Blanco
    "V": [(-1, 1, 0), (-1, 1, -2), (-1, -1, -2), (-1, -1, 0)],  # Verde
    "N": [(-1, -1, 0), (1, -1, 0), (1, -1, -2), (-1, -1, -2)],  # Naranja
    "R": [(1, 1, 0), (1, 1, -2), (1, -1, -2), (1, -1, 0)],  # Rojo
    "AZ": [(1, 1, 0), (1, 1, 2), (-1, 1, 2), (-1, 1, 0)],  # Azul
    "AM": [(1, -1, 0), (1, -1, 2), (-1, -1, 2), (-1, -1, 0)]  # Amarillo
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

class CuboTile3D(QOpenGLWidget):
    def __init__(self, x, y, size, color, cara, fila, columna):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.cara = cara
        self.fila = fila
        self.columna = columna
        self.color_actual = cara  # Inicialmente, el color es la cara (B, R, V, etc.)

    def mousePressEvent(self, event):
        if self.cara == "B" and not (self.fila == 1 and self.columna == 1):
            self.cambiar_color()
        elif self.fila == 0 and self.cara in ["V", "N", "R", "AZ"]:
            self.cambiar_color()

    def cambiar_color(self):
        indice_actual = COLORES.index(self.color_actual)
        nuevo_color = COLORES[(indice_actual + 1) % len(COLORES)]
        self.color_actual = nuevo_color
        self.update()

    def dibujar_cuadro(self):
        # Dibuja un cuadrado en la cara correspondiente usando OpenGL
        glBegin(GL_QUADS)
        color = COLORES_MAPA[self.color_actual]
        glColor3f(color.redF(), color.greenF(), color.blueF())

        for punto in CUBO_CARAS[self.cara]:
            glVertex3f(punto[0] * self.size + self.x, punto[1] * self.size + self.y, punto[2] * self.size)

        glEnd()

class Cubo3D(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cubo Rubik - Última Capa")
        self.setGeometry(100, 100, 400, 400)
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.casilla_size = 40
        self.modo_perspectiva = False
        self.estado_cubos = {} # Guardar el estado de cada casilla
        
        self.cambiar_vista_boton = QPushButton("Cambiar Vista", self)
        self.cambiar_vista_boton.setGeometry(180, 450, 120, 30)
        self.cambiar_vista_boton.clicked.connect(self.cambiar_vista)
        
        self.crear_cubo_plano()
        
    def guardar_estado(self):
        self.estado_cubos.clear()
        for item in self.scene.items():
            if isinstance(item, CuboTile):
                self.estado_cubos[(item.cara, item.fila, item.columna)] = item.color_actual
                
    def restaurar_estado(self):
        for item in self.scene.items():
            if isinstance(item, CuboTile):
                if (item.cara, item.fila, item.columna) in self.estado_cubos:
                    item.color_actual = self.estado_cubos[(item.cara, item.fila, item.columna)]
                    item.setBrush(QBrush(COLORES_MAPA[item.color_actual]))

    def crear_cubo_plano(self):
        #self.scene.clear()
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
        self.guardar_estado()
        self.scene.clear()
        
        if self.modo_perspectiva:
            self.crear_cubo_perspectiva()
        else:
            self.crear_cubo_plano()
            
        self.restaurar_estado()
        self.modo_perspectiva = not self.modo_perspectiva
            
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
    ventana = Interfaz()
    ventana.show()
    sys.exit(app.exec())
