import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,  QPushButton, QStackedWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtWidgets import QTextEdit, QHBoxLayout, QWidget, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox, QInputDialog
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
from cubo import *
from grafo import *
import random
from variables_globales import *
import traceback
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
    def __init__(self, secuencia_movimientos, historial, piecita_cambiada, cubo_modelo, movimiento_origen, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Solución paso a paso")
        self.cubo = cubo_modelo
        self.secuencia_movimientos = secuencia_movimientos
        self.historial = historial
        self.piecita_cambiada = piecita_cambiada
        self.movimiento_origen = movimiento_origen
        self.instructionsText = None
        self.current_step = 0 
        self.soluciones = [(secuencia_movimientos, historial, piecita_cambiada, movimiento_origen)]
        self.showingFullCube = False  # Estado de vista actual
        self.flip_end_shown = False  # Estado de flip mostrado al final
        

        # Layout principal horizontal
        self.mainLayout = QHBoxLayout(self)

        # Panel izquierdo: instrucciones + botones
        self.leftPanel = QWidget()
        leftLayout = QVBoxLayout(self.leftPanel)
        
        self.instructionsText = QTextEdit()
        self.instructionsText.setReadOnly(True)
        self.comentario = QTextEdit()
        self.comentario.setReadOnly(True)
        self.comentario.setText(
            "Cómo funciona la solución\n\n"
            "- Órbita canónica: Si tu cubo ya pertenece a la órbita canónica, es decir, no tiene ninguna ficha mal colocada, buscamos directamente la secuencia de giros en el grafo.\n"
            "- Otra órbita: Si detectamos una pieza desorientada, calculamos todas las orientaciones válidas, de las que hay 4 posibles en el grafo "
                "te pedimos que indiques cuál está mal para utilizar la correcta y generamos la solución desde ese nodo.\n\n"
            "El proceso en otra órbita tiene tres fases:\n"
            "  1) Corrección inicial de la pieza desorientada. Ten esto en cuenta si te guías por la imágen de la derecha\n"
            "  2) Giros canónicos para llevar la órbita a la solución.\n"
            "  3) 'Descorrección' final para devolver la pieza a su órbita original.\n\n"
            "Sigue los pasos en el panel de la derecha\n\n"
            "Muchas gracias por usar el programa y espero que te haya sido útil.\n\n"
        )
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
        self.toggleViewBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.toggleViewBtn.setAutoDefault(False)
        self.toggleViewBtn.setDefault(False)
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
        
        # flip solo si hay pieza desorientada
        self.flip_shown   = (self.piecita_cambiada is None)
        self.current_step = 0
        self.updateStep()



    def updateStep(self):
        total = len(self.secuencia_movimientos) + 2  # +1 para el flip inicial, +1 para el flip final

        # --- Paso 0: flip inicial ---
        if not self.flip_shown:
            self.instructionsText.setText(f"Paso 0/{total}:\n Muestra la arista mal orientada")
            return

        # --- Paso final: flip de vuelta ---
        if self.flip_shown and not self.flip_end_shown and self.current_step >= len(self.secuencia_movimientos):
            self.instructionsText.setText(f"Paso {len(self.secuencia_movimientos)+1}/{total}:\n Muestra la arista en órbita “mala” de nuevo")
            return

        # --- Pasos intermedios canónicos ---
        idx = self.current_step
        if idx < len(self.secuencia_movimientos):
            mov = self.secuencia_movimientos[idx]
            texto = instrucciones.get(mov, f"Movimiento desconocido: {mov}")
            # +1 porque el paso 0 ya “consumió” la posición 0
            self.instructionsText.setText(f"Paso {idx+1}/{total}:\n {texto}")
        else:
            # Después del flip final, todo completado
            self.instructionsText.setText("¡Solución completada!")
            self.nextStepBtn.setEnabled(False)
            
    def nextStep(self):
        # --- Paso 0: flip inicial ---
        if not self.flip_shown:
            orb = Orbitas(self.movimiento_origen)

            if isinstance(self.piecita_cambiada, (list, tuple)) and len(self.piecita_cambiada) == 2:
                # es una arista
                pieza = orb.buscar_posicion_por_color_arista(self.cubo,
                                                            self.piecita_cambiada)
                flip_fn = orb.flippear_arista
            else:
                # es una esquina (longitud==3)
                pieza = orb.buscar_posicion_por_color_esquina(self.cubo,
                                                            self.piecita_cambiada)
                flip_fn = orb.flippear_esquina

            if pieza:
                i, j = pieza.fila, pieza.columna

                # 1) Flippear cube_state
                cara1, cara2 = pieza.cara, pieza.adyacente.cara
                ia, ja = pieza.adyacente.fila, pieza.adyacente.columna
                # en esquinas tendrás que ajustar para la tercera cara:
                if len(self.piecita_cambiada) == 3:
                    cara3 = pieza.precedente.cara
                    ia3, ja3 = pieza.precedente.fila, pieza.precedente.columna
                    # rotación cíclica (c0,c1,c2)->(c2,c0,c1)
                    cs = cube_state
                    c0 = cs[cara1][i][j]
                    c1 = cs[cara2][ia][ja]
                    c2 = cs[cara3][ia3][ja3]
                    cs[cara1][i][j] = c2
                    cs[cara2][ia][ja] = c0
                    cs[cara3][ia3][ja3] = c1
                else:
                    # arista: swap 2
                    cs1 = cube_state[cara1]
                    cs2 = cube_state[cara2]
                    cs1[i][j], cs2[ia][ja] = cs2[ia][ja], cs1[i][j]

                # 2) Flippear el modelo molecular
                flip_fn(self.cubo, (i, j))

                # 3) Repintamos
                asignar_color_deuna(self.cubo)
                self.cube3DView.update()
                self.parent().parent().get_cubenet().drawNet()

            self.flip_shown = True
            self.updateStep()
            return

        # ------------------------------------------------
        # 2) Pasos canónicos: aplicar uno por uno
        # ------------------------------------------------
        if self.current_step < len(self.secuencia_movimientos):
            num_mov = self.historial[self.current_step]
            mov = grafo.nodos[num_mov].movimiento
            # 2.1) Aplica el giro al cube_state (estado canónico)
            traducir_a_cubo(mov, cube_state)
            # 2.2) Repinta el modelo molecular
            asignar_color_deuna(self.cubo)
            # 2.3) Actualiza vistas
            self.cube3DView.update()
            self.parent().parent().get_cubenet().drawNet()
            # 2.4) Avanza contador y refresca texto
            self.current_step += 1
            self.updateStep()
            return
        else:
            # Ya no hay más movimientos
            self.updateStep()
            
        # --- 3) Flip final (devuelve la pieza a la mala órbita) ---
        if self.flip_shown and not self.flip_end_shown and self.current_step >= len(self.secuencia_movimientos):
            orb = Orbitas(self.movimiento_origen)

            # Si es arista (2 colores)
            if isinstance(self.piecita_cambiada, (list, tuple)) and len(self.piecita_cambiada) == 2:
                pieza = orb.buscar_posicion_por_color_arista(self.cubo, self.piecita_cambiada)
                if pieza:
                    i,j = pieza.fila, pieza.columna
                    # swap en cube_state
                    cs1 = cube_state[pieza.cara]
                    cs2 = cube_state[pieza.adyacente.cara]
                    ia,ja = pieza.adyacente.fila, pieza.adyacente.columna
                    cs1[i][j], cs2[ia][ja] = cs2[ia][ja], cs1[i][j]
                    # flip molecular
                    orb.flippear_arista(self.cubo, (i,j))

            # Si es esquina (3 colores)
            else:
                pieza = orb.buscar_posicion_por_color_esquina(self.cubo, self.piecita_cambiada)
                if pieza:
                    i,j   = pieza.fila, pieza.columna
                    ia,ja = pieza.adyacente.fila, pieza.adyacente.columna
                    ip,jp = pieza.precedente.fila, pieza.precedente.columna
                    # rota cube_state cíclicamente (c0,c1,c2)->(c2,c0,c1)
                    cara0, cara1, cara2 = pieza.cara, pieza.adyacente.cara, pieza.precedente.cara
                    c0 = cube_state[cara0][i][j]
                    c1 = cube_state[cara1][ia][ja]
                    c2 = cube_state[cara2][ip][jp]
                    cube_state[cara0][i][j] = c2
                    cube_state[cara1][ia][ja] = c0
                    cube_state[cara2][ip][jp] = c1
                    # flip molecular
                    orb.flippear_esquina(self.cubo, (i,j))

            # repinta vistas
            asignar_color_deuna(self.cubo)
            self.cube3DView.update()
            self.parent().parent().get_cubenet().drawNet()

            self.flip_end_shown = True
            self.updateStep()
            return

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
        
    def openSolutionWindow(self, secuencia, historial, piecita_cambiada, movimiento_origen):
        """Crea una ventana independiente con un SolutionWidget."""
        sw = SolutionWidget(
            secuencia_movimientos=secuencia,
            historial=historial,
            piecita_cambiada=piecita_cambiada,
            cubo_modelo=self.cubo,
            movimiento_origen=movimiento_origen
        )
        win = QMainWindow(self)
        win.setWindowTitle("Solución alternativa")
        win.setCentralWidget(sw)
        win.resize(800, 600)
        win.show()

    def solucionar(self):
        # 1) Comprobamos que el cubo no está ya resuelto
        if self.cubo_solucionado():
            self.mostrarMensaje("El cubo ya está solucionado.")
            return None

        try:
            # 2) Verificar que hay exactamente 9 casillas de cada color
            counts = {}
            for face in cube_state:
                for row in cube_state[face]:
                    for color in row:
                        counts[color] = counts.get(color, 0) + 1
            for color, count in counts.items():
                if count != 9:
                    raise ValueError("Solo pueden haber 9 casillas de cada color")

            # 3) Sincronizar colores al modelo molecular
            asignar_color_deuna(self.cubo)

            # 4) Obtener representación de movimiento y buscar nodo en el grafo
            movimiento = traducir_a_mov(self.cubo)
            numero_mov = buscar_nodo(movimiento)
            escenarios = [] # guarda todas las soluciones de las órbitas

            if numero_mov is None:
                orb = Orbitas(movimiento)
                
                # --- Caso “otra órbita” ---
                self.mostrarMensaje("Movimiento no encontrado en el grafo. Es posible que estés en otra órbita.")
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Movimiento no encontrado")
                msgBox.setText("Movimiento no encontrado en el grafo. Es posible que estés en otra órbita.")
                msgBox.setInformativeText("¿Deseas continuar en otra órbita o corregir el cubo?")
                aceptar = msgBox.addButton("Continuar en otra órbita", QMessageBox.ButtonRole.AcceptRole)
                corregir = msgBox.addButton("Corregir el cubo",    QMessageBox.ButtonRole.RejectRole)
                msgBox.setDefaultButton(corregir)
                msgBox.exec()

                if msgBox.clickedButton() == aceptar:
                    
                    # 1) ---- ARISTAS (mod-2) ----
                    if not orb.comprobar_restriccion_mod2():
                        orient2 = orb.opciones_mod2_correcto()  
                        movs2 = orb.movimientos_opciones()             

                        # Preguntar al usuario si sabe qué arista flippeó:
                        etiquetas2 = [
                            f"{i+1}: {orb.buscar_color_por_posicion_arista(o, self.cubo)}"
                            for i,o in enumerate(orient2)
                        ] + ["No sé cuál flippeé"]
                        
                        elegido2, ok2 = QInputDialog.getItem(
                            self,
                            "Arista flippeada",
                            "Elige la arista que flippeaste (colores):",
                            etiquetas2,
                            0, False
                        )
                        if ok2 and elegido2 != "No sé cuál flippeé":
                            idx2 = int(elegido2.split(":")[0]) - 1
                        else:
                            # “No sé cuál” → elijo aleatoriamente
                            idx2 = random.randrange(len(orient2))
                            self.mostrarMensaje(
                                "He seleccionado una solución aleatoria para la arista."
                            )
                            
                        sel_mov2 = movs2[idx2]
                        sel_ori2 = orient2[idx2]
                        seq2, hist2 = buscar_identidad(buscar_nodo(sel_mov2))
                        col2 = orb.buscar_color_por_posicion_arista(sel_ori2, self.cubo)
                        escenarios.append((seq2, hist2, col2, sel_mov2))

                # ——— ESQUINAS (mod-3) ———
                if not orb.comprobar_restriccion_mod3():
                    orient3 = orb.opciones_mod3_correcto()  
                    movs3   = orb.movimientos_opciones_esquinas() 

                    etiquetas3 = [
                            f"{i+1}: {orb.buscar_color_por_posicion_esquina(o3, self.cubo)}"
                            for i, o3 in enumerate(orient3)
                        ] + ["No sé cuál flippeé"]
                    
                    elegido3, ok3 = QInputDialog.getItem(
                            self, "Esquina flippeada",
                            "Elige la esquina + orientación:",
                            etiquetas3, 0, False
                        )

                    if ok3 and elegido3 != "No sé cuál flippeé":
                        idx3 = int(elegido3.split(":")[0]) - 1
                    else:
                        idx3 = random.randrange(len(orient3))
                        self.mostrarMensaje(
                            "He seleccionado una solución aleatoria para la esquina."
                        )
                        
                    sel_mov3 = movs3[idx3]
                    sel_ori3 = orient3[idx3]
                    seq3, hist3 = buscar_identidad(buscar_nodo(sel_mov3))
                    col3 = orb.buscar_color_por_posicion_esquina(sel_ori3, self.cubo)
                    escenarios.append((seq3, hist3, col3, sel_mov3))

            else:
                # --- Caso canónico sin flips ---
                mov_can = grafo.nodos[numero_mov].movimiento
                seq_can, hist_can = buscar_identidad(numero_mov)
                escenarios = [(seq_can, hist_can, None, mov_can)]

            if escenarios:
                seq, hist, pieza, mov_orig = escenarios[0]
                self.solutionWidget = SolutionWidget(
                    secuencia_movimientos=seq,
                    historial=hist,
                    piecita_cambiada=pieza,
                    cubo_modelo=self.cubo,
                    movimiento_origen=mov_orig
                )
                self.stacked.addWidget(self.solutionWidget)
                self.stacked.setCurrentWidget(self.solutionWidget)

                # desactivar botones inferiores
                for btn in (self.toggleBtn, self.shuffleBtn,
                            self.reiniciarBtn, self.solucionarBtn):
                    btn.setEnabled(False)

                
            
        except Exception as e:
            traceback.print_exc()
            self.mostrarMensaje(f"Error al resolver: {e.__class__.__name__}: {e}")
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
        layout.addWidget(titulo)
        
        subtitulo = QLabel("Cuando esté listo, presione Comenzar")
        subtitulo.setObjectName("subtitleLabel")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitulo)
        
        layout.addStretch(1) # espacio bonito
        
        # Botones del menú
        self.startBtn = QPushButton("Comenzar")
        self.startBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        layout.addWidget(self.startBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.languageBtn = QPushButton("Idioma")
        self.languageBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        layout.addWidget(self.languageBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.aboutBtn = QPushButton("Acerca De")
        self.aboutBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        layout.addWidget(self.aboutBtn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.exitBtn = QPushButton("Salir")
        self.exitBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.exitBtn.clicked.connect(QApplication.instance().quit)
        layout.addWidget(self.exitBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(2)
        
        # Conexiones
        # Originará señales hacia MainContainer
        self.languageBtn.clicked.connect(self.showLanguageDialog)
        self.aboutBtn.clicked.connect(self.showAboutDialog)
        
    def showLanguageDialog(self):
        opciones = ["Español", "English"]
        idioma, ok = QInputDialog.getItem(
            self, "Seleccionar idioma", "Idioma:", opciones, 0, False
        )
        if ok:
            # Aquí puedes emitir una señal o cambiar texto de la UI
            QMessageBox.information(self, "Idioma seleccionado", f"Has seleccionado: {idioma}")

    def showAboutDialog(self):
        QMessageBox.about(
            self,
            "Acerca de Cubo Rubik",
            "<b>Cubo Rubik App</b><br>Versión 1.0<br>Desarrollado por RanaCGames<br>"
            "Este programa te permite resolver la última cara de un cubo Rubik de forma interactiva.<br>"
            "Tiene en cuenta tamnién las distintas órbitas del grupo de Rubik.<br>"
            "Es un prooyecto de TFG, Universidad Alfonso X, 2025<br>"
            "Es posible que haya errores, pero no dudes en reportarlos.<br>"
            "¡Gracias por usarlo!<br>"
        )


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

