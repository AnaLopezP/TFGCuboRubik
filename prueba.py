

class LeyGrupo():
    def __init__(self, movimiento, nombre):
        self.movimiento = movimiento
        self.nombre = nombre
    
    
    def generar_movimiento(self):
        ciclo_alpha = self.crear_ciclo()
        pos_a = self.crear_posicion_arista()
        ciclo_beta = self.crear_ciclo()
        pos_b = self.crear_posicion_verice()
        self.movimiento = [ciclo_alpha, pos_a, ciclo_beta, pos_b]
        self.nombre = input("Ingrese el nombre (los giros) del movimiento: ")
        return self.movimiento
    '''Esta funcion genera un movimiento a partir de dos ciclos y dos posiciones'''
    
    def crear_ciclo(self):
        #ciclo = []
        uno = int(input("¿A qué posición va la posición 1? "))
        dos = int(input("¿A qué posición va la posición 2? "))
        tres = int(input("¿A qué posición va la posición 3? "))
        cuatro = int(input("¿A qué posición va la posición 4? "))
        ciclo = {1: uno, 2: dos, 3: tres, 4: cuatro}
        return ciclo
    
    def crear_posicion_arista(self):
        pos = []
        for i in range(4):
            color = int(input("Ingrese 0 o 1: "))
            if color != 0 and color != 1:
                print("Error: Ingrese 0 o 1")
                return None
            pos.append(color)
            i += 1
        return pos
    '''Esta funcion indica si el color de la arista está en su lugar (0) o no (1)'''

    def crear_posicion_verice(self):
        pos = []
        for i in range(4):
            color = int(input("Ingrese 0, 1 o 2: "))
            if color != 0 and color != 1 and color != 2:
                print("Error: Ingrese 0, 1, o 2")
                break
            pos.append(color)
            i += 1
        return pos
    '''Esta funcion indica si el color del vertice está en su lugar (0), si está girado 1/3 a la izquierda (1) o 2/3 a la izquierda (2), mirándolo desde la esquina'''

    def __str__(self):
        return f"El movimiento {self.nombre} es: {self.movimiento}"
    
    def componer_movimientos(self, m1, m2):
        print(m1)
        print(m2)
        nuevo_mov = []
        nuevo_mov.append(self.componer_ciclos(m1[0], m2[0]))
        nuevo_mov.append(self.componer_posiciones_mod2(m1[1], m2[1], m2[0]))
        nuevo_mov.append(self.componer_ciclos(m1[2], m2[2]))
        nuevo_mov.append(self.componer_posiciones_mod3(m1[3], m2[3], m2[2]))
        #print(nuevo_mov)
        return nuevo_mov
        
    def componer_ciclos(self, c1, c2):
        nuevo_ciclo = {}
        for i in range(len(c1)):
            valor = c1[i+1]
            valor2 = c2[valor]
            nuevo_ciclo[i+1] = valor2
        #print(nuevo_ciclo)
        return nuevo_ciclo
    
    def calcular_ciclo_inverso(self, c2):
        ciclo_inverso = {j: i for i, j in c2.items()}  # Generar inversa
        return dict(sorted(ciclo_inverso.items()))  # Ordenarlo
    
    def componer_posiciones_mod2(self, p1, p2, c2):
        ciclo_inverso = self.calcular_ciclo_inverso(c2)
        #print("Ciclo inverso:", ciclo_inverso)

        pos = [0] * 4
        for k in range(4):
            x = ciclo_inverso[k+1]
            pos[k] = p1[x-1]
        #print("Pos mod 2:", pos)

        nueva_pos = [(pos[i] + p2[i]) % 2 for i in range(4)]
        #print("Nueva posición mod 2:", nueva_pos)
        return nueva_pos

    def componer_posiciones_mod3(self, p1, p2, c2):
        ciclo_inverso = self.calcular_ciclo_inverso(c2)
        #print("Ciclo inverso:", ciclo_inverso)

        pos = [0] * 4
        for k in range(4):
            x = ciclo_inverso[k+1]
            pos[k] = p1[x-1]
        #print("Pos mod 3:", pos)

        nueva_pos = [(pos[i] + p2[i]) % 3 for i in range(4)]
        #print("Nueva posición mod 3:", nueva_pos)
        return nueva_pos
    
    def comprobar_restricciones(self, m1):
        # primero comprobamos que el sumatorio de las posiciones de las aristas sea cero
        if sum(m1[1]) % 2 != 0:
            return False
        # luego comprobamos que el sumatorio de las posiciones de los vertices sea cero
        if sum(m1[3]) % 3 != 0:
            return False
        # por último comprobamos que la composicion de los ciclos sea la identidad
        identidad = self.componer_ciclos(m1[0], m1[2])
        if identidad != {1: 1, 2: 2, 3: 3, 4: 4}:  # si no es la identidad
            return False
        else:
            return True
        
        

    
def main():
   # en este codigo de prueba se van a crear dos movimientos m1 y m2 y se van a componer entre ellos para obtener un nuevo movimiento m3
    m1 = LeyGrupo([], "movimiento 1")
    m2 = LeyGrupo([], "movimiento 2")
    m3 = LeyGrupo([], "movimiento 3")
    print("generando el movimiento 1")
    m1.generar_movimiento()
    m1.comprobar_restricciones(m1.movimiento)
    print("generando el movimiento 2")
    m2.generar_movimiento()
    m2.comprobar_restricciones(m2.movimiento)
    print("componiendo los movimientos")
    m3 = m3.componer_movimientos(m1.movimiento, m2.movimiento)
    print("--------------------------------------------------------------------------------")
    print("                    EL MOVIMIENTO COMPUESO ES:")
    print(m3)
    print("--------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()