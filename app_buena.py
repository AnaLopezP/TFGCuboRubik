import sys, math
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,  QPushButton, QStackedWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtWidgets import QTextEdit, QHBoxLayout, QWidget
from PyQt6.QtWidgets import QTextEdit, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
from intermedio import *
from main import *
import random
from estado_cubo import cube_state

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


class SolutionWidget(QWidget):
    def __init__(self, secuencia_movimientos, historial, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Solución paso a paso")
        self.secuencia_movimientos = secuencia_movimientos
        self.historial = historial
        self.current_step = 0  # Índice del paso actual
        
        # Layout principal horizontal
        mainLayout = QHBoxLayout(self)
        
        # Panel izquierdo: instrucciones + botón de siguiente paso
        leftPanel = QWidget()
        leftLayout = QVBoxLayout(leftPanel)
        
        self.instructionsText = QTextEdit()
        self.instructionsText.setReadOnly(True)
        self.comentario = QTextEdit()
        self.comentario.setReadOnly(True)
        self.comentario.setText("¡Bienvenido a la solución del cubo Rubik!\n\n Todos los giros se hacen hacia la izquierda, en sentido antihorario, y cada giro es de 90º.\n\n :)")
        leftLayout.addWidget(self.comentario, 1)
        leftLayout.addWidget(self.instructionsText, 1)

        
        self.nextStepBtn = QPushButton("Siguiente paso")
        self.nextStepBtn.clicked.connect(self.nextStep)
        leftLayout.addWidget(self.nextStepBtn)
        
        # Panel derecho: vista 3D del cubo
        self.cube3DView = RubiksCube3D()
        
        # Agregar ambos paneles al layout principal con estiramientos
        mainLayout.addWidget(leftPanel, 2)  # Izquierda más ancha
        mainLayout.addWidget(self.cube3DView, 1)  # Derecha con vista 3D
        
        # Mostrar el primer paso (puede ser una descripción inicial)
        self.updateStep()
    
    def updateStep(self):
        """Actualiza la instrucción y aplica el siguiente movimiento (si existe)."""
        if self.current_step < len(self.secuencia_movimientos):
            mov = self.secuencia_movimientos[self.current_step]
            texto = instrucciones.get(mov, f"Movimiento desconocido: {mov}")
            self.instructionsText.setText(f"Paso {self.current_step + 1}:\n  {texto}")
            
        else:
            self.instructionsText.setText("¡Solución completada!")
            self.nextStepBtn.setEnabled(False)

    def nextStep(self):
        """Avanza al siguiente paso de la solución."""
        if self.current_step < len(self.secuencia_movimientos): 
            num_movimiento_actual = self.historial[self.current_step] 
            print("Movimiento actual numero:", num_movimiento_actual)
            # buscamos el movimiento en el grafo
            movimiento_actual = grafo.nodos[num_movimiento_actual].movimiento
            traducir_a_cubo(movimiento_actual, cube_state)
            main_widget = self.parent().parent()  # Acceder al widget principal
            if hasattr(main_widget, 'get_cubenet'):
                cubenet = main_widget.get_cubenet()
                cubenet.drawNet()
            # Actualizar la vista 3D
            self.cube3DView.update()
            self.current_step += 1  # Ahora incrementamos el paso aquí
            self.updateStep()


# ---------------------------
# Integración en la interfaz
# ---------------------------
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cubo Rubik Integrado")
        layout = QVBoxLayout(self)
        self.stacked = QStackedWidget()
        self.cubo = iniciar()
        
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
        self.reiniciarBtn = QPushButton("Reiniciar Cubo")
        self.reiniciarBtn.clicked.connect(self.reiniciarCubo)
        self.shuffleBtn = QPushButton("Mezclar")
        self.shuffleBtn.clicked.connect(self.mezclarCubo)
        
        btnLayout.addWidget(self.solucionarBtn)
        btnLayout.addWidget(self.toggleBtn)
        btnLayout.addWidget(self.reiniciarBtn)
        btnLayout.addWidget(self.shuffleBtn)
        
        layout.addLayout(btnLayout)

    def get_cubenet(self):
        return self.cubeNet
    
    def mezclarCubo(self):
        """Selecciona un nodo aleatorio del grafo y aplica los movimientos al cubo."""
        try:
            # Obtener un nodo aleatorio del grafo
            numnodo_aleatorio = random.choice(list(grafo.nodos.values()))
            print(numnodo_aleatorio)
            mov = numnodo_aleatorio.movimiento
            traducir_a_cubo(mov, cube_state)
            asignar_color_deuna(self.cubo)

            # Actualizar la vista net
            self.cubeNet.drawNet()
            # Actualizar la vista 3D
            #self.cube3D.update()
            self.mostrarMensaje("Cubo mezclado")
            
        except Exception as e:
            self.mostrarMensaje(f"Error al mezclar: {str(e)}")
            print("Error al mezclar el cubo:", e)
    
    def reiniciarCubo(self):
        # Reiniciar el cubo a su estado inicial
        # Modificar el estado del cubo en el mismo objeto, en lugar de reassignar cube_state
        for cara in cube_state:
            for i in range(3):
                for j in range(3):
                    cube_state[cara][i][j] = cara
        
        
        self.cubo = iniciar()


        self.cubeNet.drawNet()
        self.cube3D.update()
        
        # Si la vista actual es la de solución, volver a la vista original
        if isinstance(self.stacked.currentWidget(), SolutionWidget):
            self.stacked.setCurrentIndex(0)  # Volver a la vista original

        self.mostrarMensaje("Cubo reiniciado")
        return cube_state, self.cubo

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
        try:
            # Contar casillas por color
            counts = {}
            for face in cube_state:
                for row in cube_state[face]:
                    for color in row:
                        counts[color] = counts.get(color, 0) + 1

            # Verificar que cada color aparezca exactamente 9 veces
            for color, count in counts.items():
                if count != 9:
                    raise ValueError("Solo pueden haber 9 casillas de cada color")

            '''# Debug: Mostrar información de las piezas
            for i in range(3):
                for j in range(3):
                    mol = cubo[i][j]
                    if mol is not None:
                        print(mol.cara, mol.fila, mol.columna, mol.color, i, j)
                        if isinstance(mol, Vertice):
                            print(mol.adyacente.cara, mol.adyacente.fila, mol.adyacente.columna, mol.adyacente.color, i, j)
                            print(mol.precedente.cara, mol.precedente.fila, mol.precedente.columna, mol.precedente.color, i, j)
                        elif isinstance(mol, Arista):
                            print(mol.adyacente.cara, mol.adyacente.fila, mol.adyacente.columna, mol.adyacente.color, i, j)
'''
            # Convertimos el cubo a su representación de movimiento
            print(cubo)
            movimiento = traducir_a_mov(self.cubo)  # Aquí puede haber un raise
            print("Movimiento traducido:", movimiento)

            # Buscamos el nodo en el grafo
            numero_mov = buscar_nodo(movimiento)  # Aquí puede haber otro raise
            if numero_mov is None:
                raise ValueError("No se encontró un nodo en el grafo")

            #print("Número de nodo encontrado:", numero_mov)

            # Buscamos la secuencia de movimientos
            secuencia_movimientos, historial = buscar_identidad(numero_mov)
            print("Secuencia de movimientos:", secuencia_movimientos)
            print("historial de movimientos:", historial)
        
        # Si se obtuvo una solución, crear y mostrar el widget de solución
            if secuencia_movimientos is not None:
                self.solutionWidget = SolutionWidget(secuencia_movimientos, historial)
                self.stacked.addWidget(self.solutionWidget)
                self.stacked.setCurrentWidget(self.solutionWidget)
            
            return secuencia_movimientos, historial

        except Exception as e:
            self.mostrarMensaje(f"Error: {str(e)}")
            print("Error detectado:", e)
            return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = MainWidget()
        self.setMinimumSize(800, 600)
        self.setCentralWidget(self.mainWidget)
    
    def get_mainwidget(self):
        return self.mainWidget
        

if __name__ == '__main__':
    cubo = iniciar()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec())
