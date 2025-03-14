import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt

# Colores del cubito
COLORES = {
           "B": "blanco", # arriba
           "V": "verde", # izquierda
           "N": "naranja", # atrás
           "R": "rojo", # frente
           "AZ": "azul", # derecha
           "AM": "amarillo" # abajo, no editable
           }

# Estado inicial del cubo
# ESTADO_CUBO = {
#     "Cara blanca": [["B", "B", "B"],["B", "B", "B"],["B", "B", "B"]],
#     "Cara verde": [["V", "V", "V"], ["V", "V", "V"],["V", "V", "V"]],
#     "Cara naranja": [["N", "N", "N"],["N", "N", "N"],["N", "N", "N"]],
#     "Cara roja": [["R", "R", "R"],["R", "R", "R"],["R", "R", "R"]],
#     "Cara azul": [["AZ", "AZ", "AZ"],["AZ", "AZ", "AZ"],["AZ", "AZ", "AZ"]],
#     "Cara amarilla": [["AM", "AM", "AM"],["AM", "AM", "AM"],["AM", "AM", "AM"]]
# }

# coordenadas base para cada cara
POSICIONES_CARAS = {
    "Cara blanca": (100, 50),
    "Cara verde": (50, 100),
    "Cara naranja": (100, 100),
    "Cara roja": (150, 100),
    "Cara azul": (100, 150),
    "Cara amarilla": (100, 200)
}

class CuboTile(QGraphicsRectItem):
    def __init__(self, x, y, size, color, cara, fila, columna):
        super().__init__(x, y, size, size)
        self.setBrush(QBrush(QColor(color)))
        self.setPen(QPen(Qt.GlobalColor.black, 2))
        self.cara = cara
        self.color_actual = color
        self.fila = fila
        self.columna = columna
        #self.cambiar_color = cambiar_color  
    
    # funcion para cambiar los colores de una cara 
    def mousePressEvent(self, event):
        if self.face == "W" and self.row == 2:  # Solo se puede editar la última fila de la cara blanca
            self.change_color()
            
            
    def change_color(self):
        color_keys = list(COLORES.keys())
        siguiente_indice = (color_keys.index(self.color_actual) + 1) % len(color_keys)
        nuevo_color = color_keys[siguiente_indice]
        
        # Actualizar color
        self.color_actual = nuevo_color
        self.setBrush(QBrush(QColor(COLORES[nuevo_color])))

class Cubo3D(QGraphicsView):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Cubo Rubik")
        self.setGeometry(100, 100, 400, 400)
        
        # crear la escena
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        # tamaño de los cuadritos
        self.casilla_size = 40
        
        # actualizamos la vista 
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        
        # Dibujar el cubo        
        self.crear_cubo()
    
    def crear_cubo(self):
        # Dibuja las caras del cubo en perspectiva
        for face, (x, y) in POSICIONES_CARAS.items():
            for row in range(3):
                for col in range(3):
                    tile = CuboTile(
                        x + col * self.tile_size, y + row * self.tile_size,
                        self.tile_size, COLORES["W" if face == "W" else face], face, row, col
                    )
                    self.scene.addItem(tile)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cubo3D()
    window.show()
    sys.exit(app.exec())
