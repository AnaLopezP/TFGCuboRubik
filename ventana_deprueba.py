import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QBrush, QColor

class TestGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prueba QGraphicsView")
        self.setGeometry(100, 100, 400, 400)

        # Crear la escena
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        # Agregar un rectángulo de prueba
        rect = QGraphicsRectItem(0, 0, 100, 100)
        rect.setBrush(QBrush(QColor("blue")))
        self.scene.addItem(rect)

        print("Escena creada correctamente.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestGraphicsView()
    window.show()
    sys.exit(app.exec())
