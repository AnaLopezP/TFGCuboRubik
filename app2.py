import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Colores del cubo
COLORES = {
    "B": (1, 1, 1),  # Blanco (Arriba)
    "V": (0, 1, 0),  # Verde (Izquierda)
    "N": (1, 0.5, 0),  # Naranja (Atrás)
    "R": (1, 0, 0),  # Rojo (Frente)
    "AZ": (0, 0, 1),  # Azul (Derecha)
    "AM": (1, 1, 0)  # Amarillo (Abajo)
}

CUBO_CARAS = {
    "B": [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)],  # Blanco
    "V": [(-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1)],  # Verde
    "N": [(-1, -1, 1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)],  # Naranja
    "R": [(1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)],  # Rojo
    "AZ": [(1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1)],  # Azul
    "AM": [(1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, 1, -1)]  # Amarillo
}

class CuboRubik:
    def __init__(self):
        pygame.font.init()  # Inicializar Pygame para usar fuentes
        self.angulo_x = 0
        self.angulo_y = 0
        self.rotando = False
        self.ultimo_mouse_x = 0
        self.ultimo_mouse_y = 0
        self.modo_vista = "3D"
        self.fuente = pygame.font.SysFont("Arial", 24)  # Fuente para el texto
        
    def dibujar_boton(self):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, 800, 600, 0, -1, 1)  # Definir coordenadas 2D en pantalla
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Dibujar el botón con Pygame después de cambiar a 2D
        glColor3f(0.8, 0, 0)  # Rojo oscuro
        glBegin(GL_QUADS)

        # Coordenadas del botón
        glVertex2f(650, 550)
        glVertex2f(780, 550)
        glVertex2f(780, 580)
        glVertex2f(650, 580)
        glEnd()
        
        # Dibujar el texto "Cambiar Vista" en el botón usando Pygame en 2D
        text_surface = self.fuente.render("Cambiar Vista", True, (255, 255, 255))
        pygame.display.get_surface().blit(text_surface, (660, 560))

        # Restaurar el modo 3D
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

        

    def dibujar_cubo(self):
        glPushMatrix()
        glRotatef(self.angulo_x, 1, 0, 0)
        glRotatef(self.angulo_y, 0, 1, 0)

        glBegin(GL_QUADS)
        for cara, vertices in CUBO_CARAS.items():
            glColor3fv(COLORES[cara])
            for vertice in vertices:
                glVertex3fv(vertice)
        glEnd()
        
        glPopMatrix()
        
    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 650 <= mouse_x <= 780 and 550 <= mouse_y <= 580:
                    self.cambiar_vista()
                else:
                    self.rotando = True
                    self.ultimo_mouse_x, self.ultimo_mouse_y = mouse_x, mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                self.rotando = False
            elif event.type == pygame.MOUSEMOTION and self.rotando:
                nuevo_x, nuevo_y = pygame.mouse.get_pos()
                dx = nuevo_x - self.ultimo_mouse_x
                dy = nuevo_y - self.ultimo_mouse_y
                self.angulo_x += dy * 0.5
                self.angulo_y += dx * 0.5
                self.ultimo_mouse_x, self.ultimo_mouse_y = nuevo_x, nuevo_y

    def cambiar_vista(self):
        self.modo_vista = "T" if self.modo_vista == "3D" else "3D"
        print(f"Modo cambiado a: {self.modo_vista}")

    def actualizar(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self.modo_vista == "T":
            self.dibujar_plano()
        else:
            self.dibujar_cubo()
        
        self.dibujar_boton()
        pygame.display.flip()
    
    def dibujar_plano(self):
        # Aquí se implementaría la vista "desplegada" del cubo
        pass

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    cubo = CuboRubik()

    while True:
        cubo.manejar_eventos()
        cubo.actualizar()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
