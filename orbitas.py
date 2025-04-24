from cubo import Molecula, Vertice, Arista

class Orbitas:
    def __init__(self, movimiento):
        self.movimiento = movimiento
        self.orientaciones_mod2 = movimiento[1]
        self.orientaciones_mod3 = movimiento[3]

    def comprobar_restriccion_mod2(self):
        if sum(self.orientaciones_mod2) % 2 != 0:
            # no está en la órbita debido a una arista
            return False
        else:
            return True

    def opciones_mod2_correcto(self):
        if self.comprobar_restriccion_mod2() == False:
            # cambio un numero de la lista cada vez y devuelve las 4 opciones
            opciones = []
            for i in range(len(self.orientaciones_mod2)):
                if self.orientaciones_mod2[i] == 0:
                    nuevo = self.orientaciones_mod2.copy()
                    nuevo[i] = 1
                    opciones.append(nuevo)
                else:
                    nuevo = self.orientaciones_mod2.copy()
                    nuevo[i] = 0
                    opciones.append(nuevo)
            return opciones
        else:
            return False

    def movimientos_opciones(self):
        mov_opciones = []
        orientaciones = self.opciones_mod2_correcto()
        for i in range(len(orientaciones)):
            self.movimiento[1] = orientaciones[i]
            mov_opciones.append(self.movimiento.copy())            

        return mov_opciones
    
    def buscar_posicion_por_color_arista(self, cubo, colores):
        # buscamos un par de colores en el cubo
        if (cubo[0][1].color == colores[0] and cubo[0][1].adyacente.color == colores[1]) or (cubo[0][1].color == colores[1] and cubo[0][1].adyacente.color == colores[0]):
            return cubo[0][1]
        elif (cubo[1][0].color == colores[0] and cubo[1][0].adyacente.color == colores[1]) or (cubo[1][0].color == colores[1] and cubo[1][0].adyacente.color == colores[0]): 
            return cubo[1][0]
        elif (cubo[1][2].color == colores[0] and cubo[1][2].adyacente.color == colores[1]) or (cubo[1][2].color == colores[1] and cubo[1][2].adyacente.color == colores[0]):
            return cubo[1][2]
        elif (cubo[2][1].color == colores[0] and cubo[2][1].adyacente.color == colores[1]) or (cubo[2][1].color == colores[1] and cubo[2][1].adyacente.color == colores[0]):
            return cubo[2][1]
        else:
            print("No se ha encontrado la arista")
            return None
        
    def buscar_color_por_posicion_arista(self, orientacion_nueva, cubo):
        for i in range(len(self.orientaciones_mod2)):
            if self.orientaciones_mod2[i] != orientacion_nueva[i]:
                if i == 0:
                    return [cubo[0][1].color, cubo[0][1].adyacente.color]
                elif i == 1:
                    return [cubo[1][0].color, cubo[1][0].adyacente.color]
                elif i == 2:
                    return [cubo[1][2].color, cubo[1][2].adyacente.color]
                elif i == 3:
                    return [cubo[2][1].color, cubo[2][1].adyacente.color]
            else:
                print("No hay ninguna diferencia entre las orientaciones")
                
    def flippear_arista(self, cubo, posicion):
        """
        Dado el cubo (la matriz 3×3) y la posición (i,j) de la arista a voltear,
        intercambia los colores de la pieza y su adyacente.
        """
        i, j = posicion
        pieza = cubo[i][j]
        c1 = pieza.color
        c2 = pieza.adyacente.color
        pieza.color = c2
        pieza.adyacente.color = c1
        return cubo

'''    
mov = [{1: 2, 2: 1, 3: 4, 4: 3}, [1, 1, 1, 0], {1: 3, 2: 2ccfcfffdfgdfgdfgfff 1}, [2, 2, 1, 1]]
orbita = Orbitas(mov)
lista = orbita.movimientos_opciones()
for i in range(len(lista)):
    print(lista[i])fgd
    
    '''
    
def iniciar():
    cubo = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    cubo[0][0] = Vertice("B", 0, 0, "B", Molecula("R", 2, 0, "R"), Molecula("AZ", 0, 2, "AZ"))
    cubo[0][1] = Arista("B", 0, 1, "B", Molecula("R", 2, 1, "R"))
    cubo[0][2] = Vertice("B", 0, 2, "B", Molecula("V", 0, 0, "V"), Molecula("R", 2, 2, "R"))
    cubo[1][0] = Arista("B", 1, 0, "B", Molecula("AZ", 1, 2, "AZ"))
    cubo[1][1] = None
    cubo[1][2] = Arista("B", 1, 2, "B", Molecula("V", 1, 0, "V"))
    cubo[2][0] = Vertice("B", 2, 0, "B", Molecula("AZ", 2, 2, "AZ"), Molecula("N", 0, 0, "N"))
    cubo[2][1] = Arista("B", 2, 1, "B", Molecula("N", 0, 1, "N"))
    cubo[2][2] = Vertice("B", 2, 2, "B", Molecula("N", 0, 2, "N"), Molecula("V", 2, 0, "V"))
    
    return cubo

orb = Orbitas(movimiento=[{1: 2, 2: 1, 3: 4, 4: 3}, [1, 1, 1, 0], {1: 3, 2: 2, 3: 4, 4: 1}, [2, 2, 1, 1]])
cubo = iniciar()

orientacion_bien = orb.opciones_mod2_correcto()
print(orientacion_bien)
posicion = orb.buscar_color_por_posicion_arista(orientacion_bien[0], cubo)
print(posicion)