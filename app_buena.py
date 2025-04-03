import sys, math
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,  QPushButton, QStackedWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
from intermedio import *
from main import *

# ---------------------------
# Estado global del cubo
# ---------------------------
# Lista de identificadores de caras (usada para el ciclo de colores)
COLORES = ["B", "V", "N", "R", "AZ", "AM"]
COLORES_CAMBIABLES = ["B", "V", "N", "R", "AZ"]  # Solo estas caras son cambiables
# Mapa de colores (PyQt) para cada cara
COLORES_MAPA = {
    "B": QColor("white"),   # Up (Blanco)
    "V": QColor("green"),   # Left (Verde)
    "N": QColor("orange"),  # Back (Naranja)
    "R": QColor("red"),     # Front (Rojo)
    "AZ": QColor("blue"),   # Right (Azul)
    "AM": QColor("yellow")   # Down (Amarillo)
}

# Definimos nombres para las casillas según su posición
NOMBRES_ARISTAS = {(0, 1): "a", (1, 0): "b", (2, 1): "c", (1, 2): "d"}
NOMBRES_VERTICES = {(0, 0): "e", (2, 0): "f", (2, 2): "g", (0, 2): "h"}

# Definimos los colores secundarios (no el blanco) que compone cada casilla de la cara blanca según su posición
ARISTAS_LATERAL = {(0, 1): "R", (1, 0): "AZ", (2, 1): "N", (1, 2): "V"}
ESQUINAS_LATERAL = {(0, 0): ("R", "AZ"), (2, 0): ("AZ", "N"), (2, 2): ("N", "V"), (0, 2): ("V", "R")}

# Inicializamos el estado del cubo: para cada cara, una matriz 3x3 con la letra de la cara
cube_state = {cara: [[cara for _ in range(3)] for _ in range(3)] for cara in COLORES}

def colorFromLetter(letter):
    """Devuelve una tupla RGB normalizada a partir de la letra de la cara."""
    color = COLORES_MAPA[letter]
    return (color.redF(), color.greenF(), color.blueF())

# ---------------------------
# VISTA NET (plana) con QGraphicsView
# ---------------------------

POSICIONES_CARAS = {
    "R":  (3, 0),
    "AZ":  (0, 3),
    "B":  (3, 3),
    "V":  (6, 3),
    "AM": (9, 3),
    "N": (3, 6)
}
TILE_SIZE = 40

class CuboTile(QGraphicsRectItem):
    def __init__(self, x, y, size, cara, fila, columna, cube3d):
        super().__init__(x, y, size, size)
        self.cara = cara
        self.fila = fila
        self.columna = columna
        self.cube3d = cube3d
        # Color inicial: según el estado global
        self.color_actual = cube_state[cara][fila][columna]
        self.setBrush(QBrush(COLORES_MAPA[self.color_actual]))
        self.setPen(QPen(Qt.GlobalColor.black, 2))
        #self.matriz = [] # matriz de cubitos para la cara blanca
        
        '''# Vamos a guardar como objetos las casillas de la cara blanca para más tarde
        if self.cara == "B" and (self.fila !=1, self.columna != 1): # el centro no nos interesa
            # determinamos si es arista o vértice para ver la cantidad de cubitos
            if (self.fila, self.columna) in NOMBRES_ARISTAS:
                nombre = NOMBRES_ARISTAS[(self.fila, self.columna)]
                color2 = ARISTAS_LATERAL[(self.fila, self.columna)]
                # creamos el objetto cubito para la otra clase
                self.matriz.add(Cubito(nombre, "B", color2, None, self.fila, self.columna)) # añadimos el cubito a la matriz
                print(self.matriz)
                print("he pasado por aqui")
                
            elif (self.fila, self.columna) in NOMBRES_VERTICES:
                nombre = NOMBRES_VERTICES[(self.fila, self.columna)]
                color2, color3 = ESQUINAS_LATERAL[(self.fila, self.columna)]
                # creamos el objeto cubito para la otra clase
                self.matriz.add(Cubito(nombre, "B", color2, color3, self.fila, self.columna))
                print(self.matriz)
                print("he pasado por aqui")'''
                
                
    '''def get_matriz(self):
        return self.matriz'''
        
        
    def mousePressEvent(self, event):
        # Lógica de cambio de color:
        # - Si es la cara blanca ("B") y la casilla no es la central, o
        # - Si es una cara contigua a la blanca (V, N, R, AZ) y es la fila 0.
        if self.cara == "B" and not (self.fila == 1 and self.columna == 1):
            self.cambiar_color()
        elif self.cara == "R" and self.fila == 2:
            self.cambiar_color()
        elif self.cara == "AZ" and self.columna == 2:
            self.cambiar_color()
        elif self.cara == "V" and self.columna == 0:
            self.cambiar_color()
        elif self.cara == "N" and self.fila == 0:
            self.cambiar_color()
        # Actualizamos el estado global
        cube_state[self.cara][self.fila][self.columna] = self.color_actual
        print(f"Estado global actualizado: {self.cara} [{self.fila}, {self.columna}] = {self.color_actual}")
        
                
        # actualizamos la vista 3D
        self.cube3d.update()

    def cambiar_color(self):
        indice_actual = COLORES_CAMBIABLES.index(self.color_actual)
        nuevo_color = COLORES_CAMBIABLES[(indice_actual + 1) % len(COLORES_CAMBIABLES)]
        self.setBrush(QBrush(COLORES_MAPA[nuevo_color]))
        self.color_actual = nuevo_color
        asignar_color(cubo, self.cara, self.fila, self.columna, nuevo_color)

class RubiksCubeNet(QGraphicsView):
    def __init__(self, parent=None, cube3d=None):
        super().__init__(parent)
        self.setFixedSize(1000, 800)
        self.scene = QGraphicsScene()
        #self.cubo_total = 
        self.setScene(self.scene)
        self.cube3d = cube3d
        # color de fondo gris oscuro
        self.setBackgroundBrush(QColor(25, 25, 25))
        self.scene.setSceneRect(0, 0, 600, 500)
        self.tile = None
        self.drawNet()
        

    def drawNet(self):
        self.scene.clear()
        for cara, (grid_x, grid_y) in POSICIONES_CARAS.items():
            for fila in range(3):
                for col in range(3):
                    x = (grid_x + col) * TILE_SIZE
                    y = (grid_y + fila) * TILE_SIZE
                    self.tile = CuboTile(x, y, TILE_SIZE, cara, fila, col, self.cube3d)
                    self.scene.addItem(self.tile)

    
    def get_cubotile(self):
        return self.tile

# ---------------------------
# VISTA 3D con QOpenGLWidget
# ---------------------------
class RubiksCube3D(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.xRot = 0
        self.yRot = 0
        self.lastPos = QPoint()
        self.cubeSize = 2.0
        self.gap = 0.1

    def initializeGL(self):
        glClearColor(0.1, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_COLOR_MATERIAL)
        glShadeModel(GL_SMOOTH)
        glDisable(GL_LIGHTING)  # Colores planos

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w/h if h else 1, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, -25)
        glRotatef(self.xRot, 1, 0, 0)
        glRotatef(self.yRot, 0, 1, 0)
        self.drawCube()
        

    def drawCube(self):
        totalSize = 3 * self.cubeSize + 2 * self.gap
        offset = totalSize/2 - self.cubeSize/2
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    glPushMatrix()
                    x = i * (self.cubeSize + self.gap) - offset
                    y = j * (self.cubeSize + self.gap) - offset
                    z = k * (self.cubeSize + self.gap) - offset
                    glTranslatef(x, y, z)
                    self.drawSmallCube(self.cubeSize, i, j, k)
                    glPopMatrix()
                    

    def drawSmallCube(self, size, i, j, k):
        hs = size / 2

        # --- Frente (Front) ---
        glBegin(GL_QUADS)
        if k == 2:
            row = 2 - j
            col = i
            face_letter = cube_state["B"][row][col]
            glColor3f(*colorFromLetter(face_letter))
        else:
            glColor3f(0.2, 0.2, 0.2)
        glVertex3f(-hs, -hs, hs)
        glVertex3f(hs, -hs, hs)
        glVertex3f(hs, hs, hs)
        glVertex3f(-hs, hs, hs)
        glEnd()

        # --- Atrás (Back) ---
        glBegin(GL_QUADS)
        if k == 0:
            row = 2 - j
            col = 2 - i
            face_letter = cube_state["AM"][row][col]
            glColor3f(*colorFromLetter(face_letter))
        else:
            glColor3f(0.2, 0.2, 0.2)
        glVertex3f(-hs, -hs, -hs)
        glVertex3f(-hs, hs, -hs)
        glVertex3f(hs, hs, -hs)
        glVertex3f(hs, -hs, -hs)
        glEnd()

        # --- Izquierda (Left) ---
        glBegin(GL_QUADS)
        if i == 0:
            row = 2 - j
            col = k
            face_letter = cube_state["AZ"][row][col]
            glColor3f(*colorFromLetter(face_letter))
        else:
            glColor3f(0.2, 0.2, 0.2)
        glVertex3f(-hs, -hs, hs)
        glVertex3f(-hs, hs, hs)
        glVertex3f(-hs, hs, -hs)
        glVertex3f(-hs, -hs, -hs)
        glEnd()

        # --- Derecha (Right) ---
        glBegin(GL_QUADS)
        if i == 2:
            row = 2 - j
            col = 2 - k
            face_letter = cube_state["V"][row][col]
            glColor3f(*colorFromLetter(face_letter))
        else:
            glColor3f(0.2, 0.2, 0.2)
        glVertex3f(hs, -hs, hs)
        glVertex3f(hs, -hs, -hs)
        glVertex3f(hs, hs, -hs)
        glVertex3f(hs, hs, hs)
        glEnd()

        # --- Arriba (Up) ---
        glBegin(GL_QUADS)
        if j == 2:
            row = k
            col = i
            face_letter = cube_state["R"][row][col]
            glColor3f(*colorFromLetter(face_letter))
        else:
            glColor3f(0.2, 0.2, 0.2)
        glVertex3f(-hs, hs, hs)
        glVertex3f(hs, hs, hs)
        glVertex3f(hs, hs, -hs)
        glVertex3f(-hs, hs, -hs)
        glEnd()

        # --- Abajo (Down) ---
        glBegin(GL_QUADS)
        if j == 0:
            row = 2 - k
            col = i
            face_letter = cube_state["N"][row][col]
            glColor3f(*colorFromLetter(face_letter))
        else:
            glColor3f(0.2, 0.2, 0.2)
        glVertex3f(-hs, -hs, hs)
        glVertex3f(-hs, -hs, -hs)
        glVertex3f(hs, -hs, -hs)
        glVertex3f(hs, -hs, hs)
        glEnd()

    def mousePressEvent(self, event):
        self.lastPos = event.position().toPoint()

    def mouseMoveEvent(self, event):
        dx = event.position().x() - self.lastPos.x()
        dy = event.position().y() - self.lastPos.y()
        self.xRot += dy
        self.yRot += dx
        self.lastPos = event.position().toPoint()
        self.update()

# ---------------------------
# Integración en la interfaz
# ---------------------------
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cubo Rubik Integrado")
        layout = QVBoxLayout(self)
        self.stacked = QStackedWidget()
        
        # Crear ambas vistas
        self.cube3D = RubiksCube3D()
        self.cubeNet = RubiksCubeNet(cube3d=self.cube3D)
        self.stacked.addWidget(self.cube3D)
        self.stacked.addWidget(self.cubeNet)
        layout.addWidget(self.stacked)
        
        # Mensajes temporales de restricciones 
        self.messageLabel = QLabel("")
        self.messageLabel.setStyleSheet("background-color: pink; color: black; font-size: 16px; padding: 5px;")
        self.messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.messageLabel)
        self.messageLabel.hide()
        
        # Layout horizontal para botones
        btnLayout = QHBoxLayout()
        self.solucionarBtn = QPushButton("Solucionar")
        self.solucionarBtn.clicked.connect(self.solucionar)
        self.toggleBtn = QPushButton("Cambiar Vista")
        self.toggleBtn.clicked.connect(self.toggleView)
        btnLayout.addWidget(self.solucionarBtn)
        btnLayout.addWidget(self.toggleBtn)
        layout.addLayout(btnLayout)

    def get_cubenet(self):
        return self.cubeNet

    def toggleView(self):
        current = self.stacked.currentIndex()
        self.stacked.setCurrentIndex(1 - current)
        # Al cambiar de vista, se actualiza la escena (la vista net se reconstruye)
        self.cubeNet.drawNet()
        self.cube3D.update()
    
    def mostrarMensaje(self, texto):
        self.messageLabel.setText(texto)
        self.messageLabel.show()
        # Ocultar el mensaje después de 3 segundos
        QTimer.singleShot(3000, self.messageLabel.hide)

    def solucionar(self):
        # Contar las casillas por color según el estado global
        counts = {}
        for face in cube_state:
            for row in cube_state[face]:
                for color in row:
                    counts[color] = counts.get(color, 0) + 1

        # Comprobamos que cada color aparezca 9 veces
        for color, count in counts.items():
            if count != 9:
                self.mostrarMensaje("Solo pueden haber 9 casillas de cada color")
                return
            
        for i in range(3):
            for j in range(3):
                mol = cubo[i][j]
                if mol != None:
                    print(mol.cara, mol.fila, mol.columna, mol.color, i, j)
                    if isinstance(mol, Vertice):
                        print(mol.adyacente.cara, mol.adyacente.fila, mol.adyacente.columna, mol.adyacente.color, i, j)
                        print(mol.precedente.cara, mol.precedente.fila, mol.precedente.columna, mol.precedente.color, i, j)
                    
                    elif isinstance(mol, Arista):
                        print(mol.adyacente.cara, mol.adyacente.fila, mol.adyacente.columna, mol.adyacente.color, i, j)
        
        movimiento = traducir_a_mov(cubo)
        print(movimiento)
        numero_mov = buscar_nodo(movimiento)
        print(numero_mov)
        secuencia_movimientos = buscar_identidad(numero_mov)
        print("Secuencia de movimientos:", secuencia_movimientos)
        return secuencia_movimientos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)
    
    def get_mainwidget(self):
        return self.mainWidget
        

if __name__ == '__main__':
    cubo = iniciar()
    app = QApplication(sys.argv)
    window = MainWindow()
    matriz = Matriz()
    window.resize(800, 650)
    window.show()
    sys.exit(app.exec())
