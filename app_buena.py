import sys
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
from cubo import *
from grafo import *
import random
from variables_globales import *
from PyQt6.QtWidgets import QMessageBox
from orbitas import *

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
        # actualizamos la vista 3D
        self.cube3d.update()

    def cambiar_color(self):
        indice_actual = COLORES_CAMBIABLES.index(self.color_actual)
        nuevo_color = COLORES_CAMBIABLES[(indice_actual + 1) % len(COLORES_CAMBIABLES)]
        self.setBrush(QBrush(COLORES_MAPA[nuevo_color]))
        self.color_actual = nuevo_color

class RubiksCubeNet(QGraphicsView):
    def __init__(self, parent=None, cube3d=None):
        super().__init__(parent)
        self.setFixedSize(1000, 800)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.cube3d = cube3d
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
        glDisable(GL_LIGHTING) 

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
    def __init__(self, secuencia_movimientos, parent=None, *, mov_recibido=None, tipo_diferente=None, idx_diferente=None):
        super().__init__(parent)
        self.setWindowTitle("Solución paso a paso")
        self.secuencia_movimientos = secuencia_movimientos
        self.tipo_diferente = tipo_diferente
        self.idx_diferente = idx_diferente
        self.current_idx = self.idx_diferente
        self.mov_recibido = mov_recibido
        self.secuencia_movimientos = secuencia_movimientos
        self.current_step = 0 
        self.showingFullCube = False  # Estado de vista actual

        # Layout principal horizontal
        self.mainLayout = QHBoxLayout(self)

        # Panel izquierdo: instrucciones + botones
        self.leftPanel = QWidget()
        leftLayout = QVBoxLayout(self.leftPanel)
        
        self.instructionsText = QTextEdit()
        self.instructionsText.setReadOnly(True)
        self.comentario = QTextEdit()
        self.comentario.setReadOnly(True)
        self.comentario.setText("¡Bienvenido a la solución del cubo Rubik!\n\nTodos los giros son de 90º en sentido antihorario.\n\n :)")
        leftLayout.addWidget(self.comentario, 1)
        leftLayout.addWidget(self.instructionsText, 1)
        
        # Botón para pasar al siguiente paso
        self.nextStepBtn = QPushButton("Siguiente paso")
        self.nextStepBtn.clicked.connect(self.nextStep)
        leftLayout.addWidget(self.nextStepBtn)
        
        # Botón para volver a la pantalla principal
        self.volverBtn = QPushButton("Volver al menú")
        self.volverBtn.clicked.connect(self.volverMenu)
        leftLayout.addWidget(self.volverBtn)

        # Botón redondo para cambiar vista
        self.toggleViewBtn = QPushButton("<<")
        self.toggleViewBtn.setFixedSize(40, 40)
        self.toggleViewBtn.setStyleSheet("""
            QPushButton {
                border-radius: 20px;
                background-color: #E74C3C;
                color: white;
                font-weight: bold;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        self.toggleViewBtn.clicked.connect(self.toggleView)

        # Contenedor del botón para centrar verticalmente
        buttonContainer = QVBoxLayout()
        buttonContainer.addStretch()
        buttonContainer.addWidget(self.toggleViewBtn)
        buttonContainer.addStretch()

        self.middleWidget = QWidget()
        self.middleWidget.setLayout(buttonContainer)

        # Panel derecho: vista 3D del cubo
        self.cube3DView = RubiksCube3D()

        # Añadir widgets al layout principal
        self.mainLayout.addWidget(self.leftPanel, 3)
        self.mainLayout.addWidget(self.middleWidget)
        self.mainLayout.addWidget(self.cube3DView, 3)

        self.updateStep()

    def updateStep(self):
        if self.current_step < len(self.secuencia_movimientos):
            mov = self.secuencia_movimientos[self.current_step]
            texto = instrucciones.get(mov, f"Movimiento desconocido: {mov}")
            self.instructionsText.setText(f"Paso {self.current_step + 1}/{len(self.secuencia_movimientos)}:\n {texto}")
        else:
            self.instructionsText.setText("¡Solución completada!")
            self.nextStepBtn.setEnabled(False)

    def nextStep(self):
        if self.current_step >= len(self.secuencia_movimientos):
            return
        
        # --- PASO ÚNICO: tomar el movimiento directamente de la secuencia ---
        mov = self.secuencia_movimientos[self.current_step]
        traducir_a_cubo(mov, cube_state)

        # Actualizamos las vistas
        main_widget = self.parent().parent()
        if hasattr(main_widget, 'get_cubenet'):
            main_widget.get_cubenet().drawNet()
        self.cube3DView.update()

        # Avanzamos el contador y actualizamos el texto
        self.current_step += 1
        self.updateStep()
        
    def _reinsertar(self):
        """
        Saca la pieza mal orientada de la cara blanca y la coloca
        en su posición lateral/adya­cente, según mov_recibido.
        """
        idx = self.idx_diferente           # 0..3 en tus listas de orientaciones
        i = idx + 1                        # llave para net_aristas_*/net_esquinas_*
        
        # --- ARISTAS ---
        if self.tipo_diferente == 'arista':
            ori = self.mov_recibido[1][idx]  # 1 si está girada
            if ori == 1:
                # posición en cara blanca
                wb_r, wb_c = net_aristas_blanca[i]
                # posición en cara lateral
                lat_face, (lat_r, lat_c) = net_aristas_lateral[i]
                # swap blanco ↔ lateral
                cube_state["B"][wb_r][wb_c], cube_state[lat_face][lat_r][lat_c] = \
                    cube_state[lat_face][lat_r][lat_c], cube_state["B"][wb_r][wb_c]

        # --- ESQUINAS ---
        else:  # tipo_diferente == 'vertice'
            ori = self.mov_recibido[3][idx]  # 1 o 2 según dónde esté el sticker blanco
            if ori != 0:
                wb_r, wb_c = net_esquinas_blanca[i]
                if ori == 1:
                    face, (r, c) = net_esquinas_lateral1[i]
                else:  # ori == 2
                    face, (r, c) = net_esquinas_lateral2[i]
                # swap blanco ↔ adyacente
                cube_state["B"][wb_r][wb_c], cube_state[face][r][c] = \
                    cube_state[face][r][c], cube_state["B"][wb_r][wb_c]

    def volverMenu(self):
        parent = self.parent()
        while parent is not None and not isinstance(parent, MainContainer):
            parent = parent.parent()
        if parent is not None:
            parent.stacked.setCurrentIndex(0)  # Índice 0 para el menú

    def toggleView(self):
        if self.showingFullCube:
            # Volver a la vista dividida
            self.leftPanel.show()
            self.toggleViewBtn.setText("<<")
            self.mainLayout.insertWidget(0, self.leftPanel)
            self.mainLayout.insertWidget(1, self.middleWidget)
        else:
            # Ocultar panel izquierdo, mover botón al borde
            self.leftPanel.hide()
            self.toggleViewBtn.setText(">>")
            self.mainLayout.removeWidget(self.leftPanel)
            self.mainLayout.removeWidget(self.middleWidget)
            self.mainLayout.insertWidget(0, self.middleWidget)
        self.showingFullCube = not self.showingFullCube


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
        self.messageLabel.setStyleSheet("""
                                        background-color: red; 
                                        color: white; 
                                        font-size: 16px; 
                                        padding: 10px; 
                                        border-radius: 5px;
                                    """)
        self.messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.messageLabel)
        self.messageLabel.hide()
        
        # Layout horizontal para botones
        btnLayout = QHBoxLayout()
        self.solucionarBtn = QPushButton("Resolver Cubo")
        self.solucionarBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.solucionarBtn.clicked.connect(self.solucionar)
        
        self.toggleBtn = QPushButton("Alternar Vista 3D/plana")
        self.toggleBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.toggleBtn.clicked.connect(self.toggleView)
        
        self.reiniciarBtn = QPushButton("Restablecer Cubo")
        self.reiniciarBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reiniciarBtn.clicked.connect(self.reiniciarCubo)
        
        self.shuffleBtn = QPushButton("Aleatorizar Cubo")
        self.shuffleBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
            mov = numnodo_aleatorio.movimiento
            traducir_a_cubo(mov, cube_state)
            asignar_color_deuna(self.cubo)

            # Actualizar la vista net
            self.cubeNet.drawNet()
            self.mostrarMensaje("Cubo mezclado")
            
        except Exception as e:
            self.mostrarMensaje(f"Error al mezclar: {str(e)}")
            print("Error al mezclar el cubo:", e)
            
    def cubo_solucionado(self):
        # Recorremos cada cara y comprobamos que todas las casillas sean iguales a la letra de la cara.
        for cara, matriz in cube_state.items():
            for fila in matriz:
                for color in fila:
                    if color != cara:
                        return False
        return True
    
    def reiniciarCubo(self):
        
        if self.cubo_solucionado():
            self.mostrarMensaje("El cubo ya está solucionado. No se puede reiniciar.")
            return cube_state, self.cubo
        
        current_index = self.stacked.currentIndex() # la pestaña actual
        
        # Reiniciar el cubo a su estado inicial
        for cara in cube_state:
            for i in range(3):
                for j in range(3):
                    cube_state[cara][i][j] = cara
        
        self.cubo = iniciar()
        self.cubeNet.drawNet()
        self.cube3D.update()
        
        self.stacked.setCurrentIndex(current_index) # ponemos la vista actual pero reiniciada

        self.mostrarMensaje("Cubo reiniciado")
        return cube_state, self.cubo

    def toggleView(self):
        current = self.stacked.currentIndex()
        self.stacked.setCurrentIndex(1 - current)
        self.cubeNet.drawNet()
        self.cube3D.update()
    
    def mostrarMensaje(self, texto):
        self.messageLabel.setText(texto)
        self.messageLabel.show()
        QTimer.singleShot(3000, self.messageLabel.hide)
        
    def solucionar(self):
        # 1) Variables comunes (inicializamos todo para cubrir ambos casos)
        secuencia_movimientos = None
        tipo_diferente        = None
        idx_diferente         = None
        mov_recibido          = None
        
        # Comprobamos que el cubo no está solucionado
        if self.cubo_solucionado():
            self.mostrarMensaje("El cubo ya está solucionado.")
            return None

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

            asignar_color_deuna(self.cubo)  # Asignar colores a las piezas del cubo

            # Convertimos el cubo a su representación de movimiento
            movimiento = traducir_a_mov(self.cubo)  # Aquí puede haber un raise

            # Buscamos el nodo en el grafo
            numero_mov = buscar_nodo(movimiento)  # Aquí puede haber otro raise

            if numero_mov is None:
                self.mostrarMensaje("Movimiento no encontrado en el grafo. Es posible que estés en otra órbita.")

                # Mostrar ventana emergente con opciones
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Movimiento no encontrado")
                msgBox.setText("Movimiento no encontrado en el grafo. Es posible que estés en otra órbita.")
                msgBox.setInformativeText("¿Deseas continuar en otra órbita o corregir el cubo?")
                btn_otra_orbita = msgBox.addButton("Continuar en otra órbita", QMessageBox.ButtonRole.AcceptRole)
                btn_corregir = msgBox.addButton("Corregir el cubo", QMessageBox.ButtonRole.RejectRole)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)

                response = msgBox.exec()

                if msgBox.clickedButton() == btn_otra_orbita:
                    self.mostrarMensaje("Continuando en otra órbita...")
                    secuencia, historial = solucionar_otra_orbita(movimiento)

                    # le pasamos también la info de corrección al widget
                    self.solutionWidget = SolutionWidget(
                        secuencia,
                        tipo_diferente=None,
                        idx_diferente=None,
                        mov_recibido=None
                    )
                    self.stacked.addWidget(self.solutionWidget)
                    self.stacked.setCurrentWidget(self.solutionWidget)
                    
                else:
                    self.mostrarMensaje("Corrige el cubo y vuelve a intentar.")
                    return None
            else:
                # Movimiento encontrado en el grafo
                secuencia_movimientos, historial = buscar_identidad(numero_mov)

            # Si se obtuvo una solución, crear y mostrar el widget de solución
            if secuencia_movimientos is not None:
                self.solutionWidget = SolutionWidget(secuencia_movimientos, historial)
                self.stacked.addWidget(self.solutionWidget)
                self.stacked.setCurrentWidget(self.solutionWidget)
                self.toggleBtn.setEnabled(False)
                self.shuffleBtn.setEnabled(False)
                self.reiniciarBtn.setEnabled(False)
                self.solucionarBtn.setEnabled(False)

            return secuencia_movimientos, historial

        except Exception as e:
            self.mostrarMensaje(f"Error: {str(e)}")
            return None

class MainMenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        # Definir un estilo global para el menú
        self.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;  /* Color de fondo azul oscuro */
            }
            QLabel#titleLabel {
                color: #ECF0F1;    /* Texto blanco */
                font-size: 32px;
                font-weight: bold;
            }
            QLabel#subtitleLabel {
                color: #BDC3C7;   /* Gris claro */
                font-size: 18px;
            }
            QPushButton {
                background-color: #E74C3C; /* Botón rojo brillante */
                color: white;
                padding: 10px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        
        # Títulos con identificadores para aplicar estilos
        titulo = QLabel("Bienvenido al Cubo Rubik")
        titulo.setObjectName("titleLabel")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitulo = QLabel("Seleccione el idioma y presione Comenzar")
        subtitulo.setObjectName("subtitleLabel")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.startBtn = QPushButton("Comenzar")
        self.startBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        layout.addStretch(1)
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)
        layout.addStretch(1)
        layout.addWidget(self.startBtn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)


class MainContainer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stacked = QStackedWidget()

        self.menuWidget = MainMenuWidget()
        self.cubeWidget = MainWidget()  # Creamos una primera instancia (por si acaso)
        
        self.stacked.addWidget(self.menuWidget)
        self.stacked.addWidget(self.cubeWidget)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)

        # Conecta el botón de "Comenzar"
        self.menuWidget.startBtn.clicked.connect(self.startNewSession)

    def startNewSession(self):
        # Elimina el widget anterior del cubo
        self.stacked.removeWidget(self.cubeWidget)
        self.cubeWidget.deleteLater()

        # Crea una nueva instancia de MainWidget
        self.cubeWidget = MainWidget()
        self.stacked.addWidget(self.cubeWidget)
        
        # Asegúrate de que el cubo esté en su estado inicial
        for cara in cube_state:
            for i in range(3):
                for j in range(3):
                    cube_state[cara][i][j] = cara
        
        # Cambia a la nueva instancia
        self.stacked.setCurrentWidget(self.cubeWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainContainer = MainContainer()
        self.setMinimumSize(800, 600)
        self.setCentralWidget(self.mainContainer)
    
    def get_mainwidget(self):
        return self.mainWidget
    
    def keyPressEvent(self, event):
        event.ignore()
        
def run_app():
    cubo = iniciar()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

