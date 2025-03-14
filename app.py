import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt

# Colores del cubito
COLORES = {"B": "blanco",
           "V": "verde",
           "N": "naranja",
           "R": "rojo",
           "AZ": "azul",
           "AM": "amarillo"}

# Estado inicial del cubo
ESTADO_CUBO = {
    "Cara blanca": [["B", "B", "B"],["B", "B", "B"],["B", "B", "B"]],
    "Cara verde": [["V", "V", "V"], ["V", "V", "V"],["V", "V", "V"]],
    "Cara naranja": [["N", "N", "N"],["N", "N", "N"],["N", "N", "N"]],
    "Cara roja": [["R", "R", "R"],["R", "R", "R"],["R", "R", "R"]],
    "Cara azul": [["AZ", "AZ", "AZ"],["AZ", "AZ", "AZ"],["AZ", "AZ", "AZ"]],
    "Cara amarilla": [["AM", "AM", "AM"],["AM", "AM", "AM"],["AM", "AM", "AM"]]
}

class Cubo3D(QGraphicsView):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Cubo Rubik")
        self.setGeometry(100, 100, 600, 600)
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.dibujar_cubo()
    
    def dibujar_cubo(self):
        # Dibuja las caras del cubo en perspectiva
        size = 50 # Tamaño de los cuuadritos
        spacing = 5 # Espacio entre cuadritos
        
        # coordenadas base para cada cara
        posiciones_cara = {
            "Cara blanca": (150, 50),
            "Cara verde": (0, 200),
            "Cara naranja": (460, 200),
            "Cara roja": (150, 200),
            "Cara azul": (305, 200),
            "Cara amarilla": (150, 350)
        }
        
        self.cuadritos = {} # Almacenamos los cuadritos en un diccionario para poder modificarlos después
        
        for cara, (x_start, y_start) in posiciones_cara.items():
            self.cuadritos[cara] = []
            
            for i in range(3):
                fila = []
                for j in range(3):
                    color = COLORES[ESTADO_CUBO[cara][i][j]]
                    cuadrito = QGraphicsRectItem(x_start + j * (size + spacing),
                                               y_start + i * (size + spacing),
                                               size, size)
                    cuadrito.setBrush(QBrush(QColor(color)))
                    cuadrito.setPen(Qt.PenStyle.NoPen)
                    self.scene.addItem(cuadrito)
                    
                    # Permitimos editar los bloques de la cara blanca
                    if cara == "Cara blanca":
                        cuadrito.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable)
                        cuadrito.mousePressEvent = lambda event, i= i, j= j: self.cambiar_color("Cara blanca", i, j)
                    
                    fila.append(cuadrito)
                self.cuadritos[cara].append(fila)
        
    def cambiar_color(self, cara, i, j):
        # Cambia el color del cuadrito seleccionado en la cara blanca
        colores = list(COLORES.keys())
        color_actual = ESTADO_CUBO[cara][i][j]
        nuevo_color = colores[(colores.index(color_actual) + 1) % len(colores)]
        ESTADO_CUBO[cara][i][j] = nuevo_color
        self.cuadritos[cara][i][j].setBrush(QBrush(QColor(COLORES[nuevo_color])))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cubo3D()
    window.show()
    sys.exit(app.exec())
