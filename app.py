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

        
if __name__ == "__main__":
    None
